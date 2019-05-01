from django.urls import path
from django.urls import include
from .views import PlaceViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'places', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls))
]