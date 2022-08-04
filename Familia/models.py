from django.db import models

# Create your models here.
class Listado(models.Model):
    familiar = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
