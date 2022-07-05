from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(max_length=20)
    stock = models.IntegerField(max_length=20)
    imagen = models.CharField(max_length=400, default= "imagen" )

class Usuario(models.Model):
    nombre = models.CharField(max_length=16, null=False)
    apellido = models.CharField(max_length=16, null=False)
    email = models.EmailField(primary_key=True, unique=True)
    ciudad = models.CharField(max_length=30, null=False)
    pwd = models.CharField(null=False, max_length=12)

class Descuento(models.Model):
    id = models.IntegerField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=40)
    porcentaje = models.IntegerField(max_length=3)

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    username = models.EmailField(null=False)
    subtotal = models.IntegerField(null=False)


class CarritoItem(models.Model):
    id_carrito = models.IntegerField(null=False)
    id_producto = models.IntegerField(null=False)
    nombre = models.CharField(null=False, max_length=30)
    cantidad = models.IntegerField(null = False)
    subtotal_producto = models.IntegerField(null=False)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    usuario = models.EmailField(null=False)
    fecha = models.DateField(null=False)
    total = models.IntegerField(null=False)