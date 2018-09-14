from django.shortcuts import render
from rest_framework import generics, viewsets
from home.models import Applications
from .serializers import ApplicationsSerializer, UserSerializer
from users.models import CustomUser


class ListApplicationsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer