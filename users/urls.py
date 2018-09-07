from django.urls import path
from . import views
#from .forms import LoginForm

# app namespace
app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('login/', views.login, name='login2'),
]