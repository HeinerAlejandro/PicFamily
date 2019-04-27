from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .models import Place
from .serializers import PlaceSerializer

# Create your views here.

class PlacesView(APIView):

    def get(self, *args, **kwargs):

        places = Place.objects.all()
        serializer = PlaceSerializer(places, many = True)

        return Response(serializer.data, status = HTTP_200_OK)

