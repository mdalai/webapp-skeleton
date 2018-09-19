from django.urls import path, include
from .views import UserViewSet #,ListApplicationsView
from  restapi import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
from django.conf.urls import url


urlpatterns = [
    #path('apps/', ListApplicationsView.as_view(), name="apps-all"),
    #path('apps_def/', views.app_list, name="apps-list-def"),
    #url(r'^apps_def/(?P<pk>[0-9]+)/$', views.app_detail, name="app-detail"),
    path('apps/', views.AppList.as_view(), name="apps-list"),
    url(r'^apps/(?P<pk>[0-9]+)/$', views.AppDetail.as_view(), name="app-detail"),
    #path('users/', UserViewSet.as_view(), name="users-all"),
]

urlpatterns = format_suffix_patterns(urlpatterns)



#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    #url(r'^', include(router.urls)),
    url(r'^users/$', views.UserList.as_view(), name='customuser-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='customuser-detail'),
]