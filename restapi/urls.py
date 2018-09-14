from django.urls import path, include
from .views import ListApplicationsView,UserViewSet


urlpatterns = [
    path('apps/', ListApplicationsView.as_view(), name="apps-all"),
    #path('users/', UserViewSet.as_view(), name="users-all"),
]


from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]