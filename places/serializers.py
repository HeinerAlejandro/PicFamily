from rest_framework import serializers
from .models import Place, Reservation

class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Place

        fields = (
            'title',
            'presentation',
            'rating',
            'posts'
        )

class ReservationSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reservation
        fields = '__all__'
