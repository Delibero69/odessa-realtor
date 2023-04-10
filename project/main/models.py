from django.db import models
import logging

# Create your models here.
class building(models.Model):
    title = models.CharField(max_length=255)
    etaj = models.CharField(max_length=255)
    sekciya = models.CharField(max_length=255)
    ploshad = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
