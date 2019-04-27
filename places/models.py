from django.db import models

# Create your models here.

def upload_image_of_place(instance, filename):
    return '{}/{}'.format(instance.title, filename)

class Place(models.Model):

    title = models.CharField(max_length = 20)
    presentation = models.ImageField(upload_to = upload_image_of_place)
    rating = models.DecimalField(max_digits = 2, decimal_places = 1, default = 0.0)
    added = models.DateTimeField(auto_now_add = True)
    posts = models.IntegerField(default = 10)