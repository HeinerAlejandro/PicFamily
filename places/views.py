from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.

class PlaceViewSet(ModelViewSet):
    
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()