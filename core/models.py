from django.db import models

# Create your models here.


#class Carro():

# class Historial():

# class Producto():
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=20)
    stock = models.IntegerField(max_length=20)

# class Usuario():

