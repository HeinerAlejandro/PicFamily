from rest_framework.permissions import BasePermission
from .models import Reservation
from datetime import datetime

class IsAuthenticatedToRegisterProduct(BasePermission):

    def has_permission(self, request, view):

        if request.method == 'post' and not request.user:
            return False
        
        return True
    

class hasPosts(BasePermission):

    def has_object_permission(self, request, view, obj):

        message = "{0} no tiene mas espacio".format(obj.title)

        date = obj.date

        try:
            
            reservation = Reservation.objects.get(date = date)

            return False

        except Exception:
            pass
        
        return True

class isValidDateReservation(BasePermission):

    def has_permission(self, request, view):

        today = datetime.today()

        date = request.data['date']

        comparison = date >= str(today)
        
        return comparison