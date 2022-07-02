from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def home(request):
    contexto = {'producto': Producto.objects.all()}
    return render(request, 'core/index.html', contexto)

def registrarProducto(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    precio=request.POST['precio']
    stock=request.POST['stock']

        
    productos = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, stock=stock)
    return redirect('/')
    

def actualizarProducto(request, codigo):
    productos = Producto.objects.get(codigo=codigo)
    return render(request, 'core/actualizarProducto.html', {'productos':productos})
       

def eliminarProducto(request, codigo):
    productos = Producto.objects.get(codigo=codigo)
    productos.delete()
    return redirect('/')

