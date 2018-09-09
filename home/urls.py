from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
  path('', views.index, name='index'),
  #path('', views.HomeView.as_view(), name='index'),
  path('add-app-form/', views.AppUserFormView.as_view(), name='add-app-form'),
  path('delete/<int:app_id>/', views.delete, name='delete'),
  path('sort/', views.sort, name='sort'),
]