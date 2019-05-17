from django.urls import path
from django.urls import include
from .views import ProductsViewSet, OrderViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'products', ProductsViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
