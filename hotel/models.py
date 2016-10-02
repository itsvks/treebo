from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Deals(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    rating = models.FloatField()
    link = models.CharField(max_length=255)
    actual_price = models.FloatField()
    discount = models.IntegerField()
    location = models.CharField(max_length=255)
