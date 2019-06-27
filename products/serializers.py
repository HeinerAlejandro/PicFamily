from rest_framework import serializers
from .models import ProductModel
from .models import order
from .models import OperationBuy

class ProductModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductModel
        fields = ('title', 'categorie','presentation', 'description', 'price')

class OperationModelSerializer(serializers.ModelSerializer):


    class Meta:

        model =  OperationBuy
        fields = '__all__'

class OrderModelSerializer(serializers.ModelSerializer):

    products =  OperationModelSerializer(source = 'operationbuy_set', read_only = True, many = True)

    class Meta: 
        model = order
        fields = '__all__'