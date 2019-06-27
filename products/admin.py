from django.contrib import admin

from .models import ProductModel
from .models import OperationBuy
from .models import Categorie
from .models import order
from rest_framework import reverse


# Register your models here.


class OrderModelAdmin(admin.ModelAdmin):

    def view_on_site(self, obj):
        
        return reverse('order')

    list_display = (
        'user',
        'TotalPrice',
        'getSelectComponenetToProducts',
        'date'
    )

    readonly_fields = (
        'user',
        'TotalPrice',
        'getSelectComponenetToProducts',
        'date'
    )

    search_fields = (
        'operationbuy__product__title',
        'user__username'
    )

admin.site.register(Categorie)
admin.site.register(ProductModel)
admin.site.register(OperationBuy)
admin.site.register(order, OrderModelAdmin)