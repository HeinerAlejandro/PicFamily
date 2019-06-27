from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Place, Reservation
from .serializers import PlaceSerializer, ReservationSerializer
from rest_framework import reverse
from datetime import datetime
from .permissions import hasPosts, isValidDateReservation, IsAuthenticatedToRegisterProduct
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import F
from rest_framework import mixins
import json

# Create your views here.

ReservationPermissions = [
    permissions.IsAdminUser,
    hasPosts,
    isValidDateReservation
]


class ReservationViewSet(mixins.ListModelMixin,
                        GenericViewSet):

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class PlaceViewSet(ModelViewSet):
    
    permission_classes = [
        IsAuthenticatedToRegisterProduct
    ]

    serializer_class = PlaceSerializer
    serializer_class_reservations = ReservationSerializer
    queryset = Place.objects.all()

    lookup_field = 'title'
    lookup_url_kwarg = 'title'

    def getFieldsForTypeUser(self):

        fields = (
            'title',
            'presentation',
            'rating',
            'posts'
        )

        user = self.request.user

        if user and user.is_staff == True:
            return False

        return fields

    def list(self, *args, **kwargs):
        
        placeSerializerClass = self.get_serializer_class()

        fields = self.getFieldsForTypeUser()

        places = self.get_queryset()

        if not fields:

            placeSerializer = placeSerializerClass(places, many = True)

            return Response(placeSerializer.data, status = status.HTTP_200_OK)
        
        placeSerializer = placeSerializerClass(places, fields = fields, many = True)

        return Response(placeSerializer.data, status = status.HTTP_200_OK)


    @action(detail = False, methods = ['get'], permission_classes = [permissions.IsAuthenticated])
    def reservations(self, request):

        reservations =  Reservation.objects.all()

        user = self.request.user

        if not user.is_staff:
            reservations = reservations.filter(user = user)

        reservationSerializer = ReservationSerializer(reservations, many = True)

        return Response(reservationSerializer.data, status = status.HTTP_200_OK)


    @action(detail = True, methods = ['get'], permission_classes = [permissions.IsAdminUser], url_path = 'reservations', url_name = 'respective-reservations')
    def getRespectiveReservation(self, request, title):

        place = self.get_object()

        placeSerializerClass = self.serializer_class

        placeSerializer = placeSerializerClass(place)
  
        reservations = placeSerializer.data.get('reservations')

        return Response(reservations, status = status.HTTP_200_OK)

    @action(detail = True, methods = ['post'], permission_classes = ReservationPermissions, url_path = 'reservations')
    def createReservation(self, request, title):

        date = self.request.data.get('date', None)

        if title and date:
    
            places = Place.objects.all()

            place = get_object_or_404(self.queryset, title = title)

            Reservation.objects.create(
                place = place,
                date = date,
                user = self.request.user
            )

            place.posts = F('posts') - 1
            place.save()

            message = { 'detail' : "Reservacion realizada con exito" }

            content_type = 'application/json'

            return Response(message, status = status.HTTP_200_OK, content_type = content_type)

        return Response(status = status.HTTP_400_BAD_REQUEST)
