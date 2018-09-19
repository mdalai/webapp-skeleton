from django.shortcuts import render
from rest_framework import generics, viewsets
from home.models import Applications
from .serializers import ApplicationsSerializer, UserSerializer
from users.models import CustomUser


from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

from rest_framework import permissions
from .permissions import IsAdminOrReadOnly




# class-based views ----------------------------------------------------------------------------
class ListApplicationsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer

class AppList(generics.ListCreateAPIView):
    """
    List all applications, or create a new app.
    """
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)

    '''
    def get(self, request, format=None):
        apps = Applications.objects.all()
        serializer = ApplicationsSerializer(apps, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    '''
class AppDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a app instance.
    """
    queryset = Applications.objects.all()
    serializer_class = ApplicationsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
    #permission_classes = (permissions.IsAdminUser,)

    '''
    def get_object(self, pk):
        try:
            return Applications.objects.get(pk=pk)
        except Applications.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = ApplicationsSerializer(app)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        app = self.get_object(pk)
        serializer = ApplicationsSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        app = self.get_object(pk)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# function-based views -------------------------------------------------------------------------
'''
#@csrf_exempt
@api_view(['GET','POST'])
def app_list(request, format=None):
    """
    List all applications, or create a new app.
    """
    if request.method == 'GET':
        apps = Applications.objects.all()
        serializer = ApplicationsSerializer(apps, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.errors, status=400)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def app_detail(request, pk, format=None):
    """
    Retrieve, update or delete a app.
    """
    try:
        app = Applications.objects.get(pk=pk)
    except Applications.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApplicationsSerializer(app)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        serializer = ApplicationsSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        app.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''