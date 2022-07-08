from pyexpat import model
from django.db import models

# Create your models here.

class Descuento(models.Model):
    id_descuento = models.IntegerField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    porcentaje = models.IntegerField(max_length=3)
    codigo = models.IntegerField(max_length=5, default=0, null=True)

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=20)
    precio_antiguo = models.IntegerField(max_length=20, default=0)
    estado_promocion = models.BooleanField(default=False)
    stock = models.IntegerField(max_length=20)
    imagen = models.CharField(max_length=400, default= "imagen" )

    def __str__(self) -> str:
        return f'{self.nombre} -> {self.precio}' 

class Usuario(models.Model):
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField(max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    ciudad = models.CharField(max_length=30, null=False)
    pwd = models.CharField(null=False, max_length=12)

class Historial(models.Model):
    codigo = models.AutoField(primary_key=True)
    precio = models.IntegerField(max_length=20)
    fecha = models.DateField(null=False)

class Suscripcion(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    fecha = models.DateField(null = False)
    descuento = models.IntegerField(default=5)
    monto = models.IntegerField(default=0)
