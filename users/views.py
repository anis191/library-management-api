from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import SimpleUserSerializers

# Create your views here.
class SimpleUserViewSet(ModelViewSet):
    http_method_names = ['get','put','delete']

    queryset = User.objects.all()
    serializer_class = SimpleUserSerializers
    
