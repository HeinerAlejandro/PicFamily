from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import ProductModel, order, OperationBuy
from .serializers import ProductModelSerializer, OrderModelSerializer
# Create your views here.

class ProductsViewSet(ModelViewSet):

    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()

class OrderViewSet(ModelViewSet):

    permissions = [
        permissions.IsAuthenticated
    ]

    serializer_class = order
    queryset = order.objects.all()

    def getObjectProductFromData(self, product, order):
        
        productModelInstane = ProductModel.objects.get(title = product.get('name', None))

        cant = product.get('cant', None)

        operationModelInstance = OperationBuy.objects.create(
            product = productModelInstane,
            q = cant,
            order = order
        )

        return operationModelInstance

    def create(self, *args, **kwargs):

        orderFromClient = self.request.data

        if orderFromClient:

            products = orderFromClient.get('order', None)
           
            total = orderFromClient.get('total', None)

            productModelInstances = []

            Order = order.objects.create(
                user = self.request.user,
                TotalPrice = total  
            )

            for product in products:
                self.getObjectProductFromData(product, Order)

            return Response(status = status.HTTP_200_OK)
        
        return Response(status = status.HTTP_400_BAD_REQUEST)
            
