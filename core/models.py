from django.db import models


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

class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=14)
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField(max_length=16, null=False)
    email = models.EmailField(null=False, unique=True)
    pwd = models.CharField(null=False, max_length=12)