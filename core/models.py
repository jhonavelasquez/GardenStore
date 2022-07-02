from django.db import models
from numpy import imag

# Create your models here.


#class Carro():

# class Historial():

# class Producto():
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=20)
    stock = models.IntegerField(max_length=20)
    imagen = models.CharField(max_length=400, default= "imagen" )

# class Usuario():

