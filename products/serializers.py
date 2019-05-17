from rest_framework import serializers
from .models import ProductModel
from .models import order

class ProductModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductModel
        fields = ('title', 'categorie','presentation', 'description', 'price')

class OrderModelSerializer(serializers.ModelSerializer):

    class Meta: 
        model = order
        fields = '__all__'