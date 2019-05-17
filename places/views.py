from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Place, Reservation
from .serializers import PlaceSerializer, ReservationSerializer

# Create your views here.

class PlaceViewSet(ModelViewSet):
    
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

class ReservationViewSet(ModelViewSet):

    permissions_class = [
        permissions.IsAuthenticated,
    ]

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def create(self, *args, **kwargs):

        date = self.request.data.get('date')

        exist_reservation = Reservation.objects.filter(date = date).exists()

        if not exist_reservation:

            title = self.request.data.get('title', None)

            place = None

            if title:

                place = Place.objects.get(title = title)

                Reservation.objects.create(
                    place = place,
                    date = date,
                    user = self.request.user
                )

                return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)