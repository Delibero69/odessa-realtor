from django.db import models
import logging


class Category(models.Model):
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
    def __str__(self):
        return self.name


# Create your models here.
class building(models.Model):
    title = models.CharField(max_length=255, blank=True)
    rooms = models.CharField(max_length=255, blank=True)
    etaj = models.CharField(max_length=255, blank=True)
    sekciya = models.CharField(max_length=255, blank=True)
    ploshad = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    bathroom = models.CharField(max_length=255, blank=True)
    kitchen = models.CharField(max_length=255, blank=True)
    paradnaya = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
