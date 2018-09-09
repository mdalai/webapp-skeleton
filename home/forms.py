from django import forms
from django.db import connection
from django.http import Http404
from .models import Userapps, Applications
from users.models import CustomUser
from django.db.models import Max

def get_choices(userid):
    with connection.cursor() as cursor:
        rows = cursor.execute('''SELECT id, name || ' | ' || description FROM
                            applications WHERE id NOT IN (
                                SELECT app_id_id FROM userapps WHERE user_id_id = {}
                            )
                            '''.format(userid)).fetchall()
    return rows

class AppUserForm(forms.Form): 
    app = forms.ChoiceField( required=True)   

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AppUserForm, self).__init__(*args, **kwargs)
        #print("Form Init User ID: {}".format(self.user))
        choices = get_choices(self.user)
        self.fields['app'].choices = choices


    def save(self, userid, commit=True):
        data = self.cleaned_data
        try:
            appid = data['app']
        except LookupError:
            raise Http404        
        max_place_order = Userapps.objects.filter(user_id=userid).aggregate(Max('place_order'))['place_order__max']
        placeorder = 1 if max_place_order is None else max_place_order+1

        #print("SAVE PLACE ORDER: ", placeorder)
        #print("SAVE APP ID: ", appid)
        #print("SAVE USER ID: ", userid)

        user = CustomUser(pk=userid)
        app = Applications(pk=appid)
        userapp = Userapps(user_id=user, app_id=app, place_order=placeorder)
        userapp.save()