from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

def upload_image_of_product(instance, filename):
    return '{}/{}'.format(instance.categorie, filename)

class Categorie(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class ProductModel(models.Model):
    
    title = models.CharField(verbose_name = 'Titulo', max_length= 70)
    presentation = models.ImageField(verbose_name = 'Presentacion', upload_to = upload_image_of_product)
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(verbose_name = 'Precio', max_digits = 20, decimal_places = 2)
    date_register = models.DateTimeField(verbose_name = 'Fecha de registro', auto_now_add = True)
    date_updated = models.DateTimeField(verbose_name = 'Fecha de actualizacion', auto_now = True)
    stock = models.IntegerField(verbose_name = 'cantidad')

    def __str__(self):
        return '{} x{}'.format(self.title, self.stock)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class OperationBuy(models.Model):
    q = models.IntegerField(verbose_name = 'Cantidad')
    product = models.ForeignKey(ProductModel, verbose_name = "producto", on_delete = models.CASCADE)
    order = models.ForeignKey('order', verbose_name = 'Orden de compra', on_delete = models.CASCADE)

    def __str__(self):
        return '{}'.format(self.pk)

    class Meta:
        verbose_name = 'Operacion de venta'
        verbose_name_plural = 'Lugares'

class order(models.Model):

    user = models.ForeignKey(user, verbose_name = "Orden", on_delete = models.CASCADE, unique = False)
    TotalPrice = models.DecimalField(verbose_name = 'Precio', max_digits = 20, decimal_places = 2)
    date = models.DateTimeField(verbose_name = '', auto_now_add = True)

    def __str__(self):
        return '{}'.format(self.pk)

    class Meta:
        verbose_name = 'Orden de compra'
        verbose_name_plural = 'Ordenes de compra'