from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm



class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


'''
from .forms import LoginForm
def login(request):
    form = LoginForm   
    return render(request, 'registration/login.html', {'form': form})
'''