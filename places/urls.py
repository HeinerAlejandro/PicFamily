from django.urls import path
from django.urls import include
from .views import PlaceViewSet, ReservationViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'places', PlaceViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls))
]