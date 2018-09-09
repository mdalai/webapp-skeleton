from django.shortcuts import render, redirect

from django.views.generic import FormView,TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#import json
from .models import Userapps, Applications
from django.db import connection

from .forms import AppUserForm

#class HomeView(TemplateView):
#  template_name = 'home/index.html'


class AjaxTemplateMixin(object):    
  def dispatch(self, request, *args, **kwargs):
      if not hasattr(self, 'ajax_template_name'):
          split = self.template_name.split('.html')
          split[-1] = '_inner'
          split.append('.html')
          self.ajax_template_name = ''.join(split)
      if request.is_ajax():
          self.template_name = self.ajax_template_name
      return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


class AppUserFormView(SuccessMessageMixin, AjaxTemplateMixin,FormView):
    template_name = 'home/add_app_form.html'
    form_class = AppUserForm
    success_url = reverse_lazy('home:index')
    #success_message = "Way to go!"

    # initialize the form choicefields 
    def get_form_kwargs(self):
        kwargs = super(AppUserFormView, self).get_form_kwargs()
        kwargs['user'] = self.request.user.id
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #print(form.cleaned_data['app'])
        form.save(self.request.user.id)
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        #form_class = self.get_form_class()
        #form = self.get_form(form_class)
        #context = self.get_context_data(**kwargs)
        #context['form'] = form
        #print("GET: {}/{}".format(request.user.id,request.user.username))
        return super().get(request, *args, **kwargs)

    '''
    def get_success_url(self):
        return reverse('home:index')

    def post(self, request, *args, **kwargs):
        print("POST: {}/{}".format(request.user.id,request.user.username))
        form = self.get_form()
        return super().post(request, *args, **kwargs)
    
    '''

def get_userapps(userid):
    if userid is None:
        return None
    with connection.cursor() as cursor:
        rows = cursor.execute('''SELECT applications.id,
                                name, description, color, defaultstatus, link, place_order FROM applications 
                            INNER JOIN userapps ON (userapps.app_id_id=applications.id 
                                and userapps.user_id_id = {})
                            ORDER BY place_order
                            '''.format(userid)).fetchall()
        if rows == []:
            data = cursor.execute("SELECT id FROM applications WHERE defaultstatus=1").fetchall()
            data = [(i+1,)+d+(userid,) for i,d in enumerate(data)]
            #print(data)
            cursor.executemany('''INSERT INTO userapps(place_order,app_id_id,user_id_id) 
                                VALUES (?,?,?)''',data)
            rows = cursor.execute('''SELECT applications.id,
                                name, description, color, defaultstatus, link, place_order FROM applications 
                            INNER JOIN userapps ON (userapps.app_id_id=applications.id 
                                and userapps.user_id_id = {})
                            ORDER BY place_order
                            '''.format(userid)).fetchall()


    return rows

# Create your views here.
def index(request):
    userid = request.user.id
    userapps = get_userapps(userid)
    context = {
        'title': 'Home Page',
        'userapps_list': userapps,
    }
    return render(request, 'home/index.html', context=context)

from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def delete(request, app_id):
    userid = request.user.id
    Userapps.objects.filter(app_id=app_id,user_id=userid).delete()
    return redirect('home:index')

@csrf_exempt
def sort(request):
    userid = request.user.id
    #print("INDEX userid: ",userid)
    orders = request.GET.get('order', None)
    orders = orders.split(',')
    orders.pop()  # delete a empty str
    orders = [int(i) for i in orders]
    #print("INDEX order: ", orders)
    for i,order in enumerate(orders):
        #print(order, i+1)
        Userapps.objects.filter(user_id=userid,app_id=order).update(place_order=i+1)
    return redirect('home:index') 


