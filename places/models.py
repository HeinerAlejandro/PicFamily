from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

def upload_image_of_place(instance, filename):
    return '{}/{}'.format(instance.title, filename)

class Place(models.Model):

    title = models.CharField(max_length = 20)
    presentation = models.ImageField(upload_to = upload_image_of_place)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, default = 0.0)
    added = models.DateTimeField(auto_now_add = True)
    posts = models.IntegerField(default = 10)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'


reservable = (
    ('Si', True),
    ('No', False)
)

class Reservation(models.Model):

    user = models.ForeignKey(user, verbose_name = 'Usuario', on_delete = models.CASCADE)
    place = models.ForeignKey(Place, verbose_name = 'Lugar', on_delete = models.CASCADE)
    date = models.DateField(verbose_name = 'reservacion')
    price = models.DecimalField(verbose_name = 'Precio', max_digits = 20, decimal_places = 2, default = 10.23)
