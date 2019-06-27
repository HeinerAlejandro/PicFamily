from rest_framework import serializers
from .models import Place, Reservation
from authentication.serializers import UserSerializer

class ReservationSerializer(serializers.ModelSerializer):

    user = serializers.CharField(source = 'user.username')

    class Meta:

        model = Reservation
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    

    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)

        super(PlaceSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
        
            allowed = set(fields)
            existing = set(self.fields)
            
            for field_name in existing - allowed:
                self.fields.pop(field_name)

  
    reservations = ReservationSerializer(source = 'reservation_set', read_only = True, many = True)

    class Meta:
        
        model = Place

        fields = (
            'title',
            'presentation',
            'rating',
            'posts',
            'reservations'
        )