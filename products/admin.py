from django.contrib import admin

from .models import ProductModel
from .models import OperationBuy
from .models import Categorie
from .models import order


# Register your models here.

admin.site.register(Categorie)
admin.site.register(ProductModel)
admin.site.register(OperationBuy)
admin.site.register(order)