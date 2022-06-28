from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.marca+" "+self.patente

#class Carro():

# class Historial():

# class Producto():

# class Usuario():

