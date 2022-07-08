
from datetime import datetime
from xmlrpc.client import DateTime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from .models import *
from core.models import Producto
from .Carrito import *
from django.contrib.auth.models import User



def home(request):
    contexto = {'producto': Producto.objects.all()}
    # user = User.objects.all(id= request.session.keys())
    # if user.is_staff == 1:
    #     return render(request, 'core/indexADMIN.html', contexto)
    return render(request, 'core/index.html', contexto)

def homeAdmin(request):
    contexto = {'producto': Producto.objects.all()}
    return render(request, 'core/indexADMIN.html', contexto)

def crudProducto(request):
    contexto = {'producto': Producto.objects.all()}
    return render(request, 'core/crud_productos.html', contexto)


def crudDescuento(request):
    contexto = {'descuento': Descuento.objects.all()}
    return render(request, 'core/crud_descuentos.html', contexto)

def historial(request):
    contexto = {'historial': Historial.objects.all()}
    return render(request, 'core/historial.html', contexto)

def suscripcion(request):
    return render(request, 'core/suscripcion.html')

def carro(request):
    return render(request, 'core/carro.html')

def registrarProducto(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    precio=request.POST['precio']
    stock=request.POST['stock']
    imagen=request.POST['imagen']

        
    productos = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, stock=stock, imagen=imagen)
    return redirect('homeAdmin')

def actualizarProducto(request, codigo):
    productos = Producto.objects.get(codigo=codigo)
    return render(request, 'core/actualizar_productos.html', {'productos':productos})

def editarProducto(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    precio=request.POST['precio']
    stock=request.POST['stock']
    imagen=request.POST['imagen']
    
    productos = Producto.objects.get(codigo=codigo)
    productos.nombre = nombre
    productos.precio = precio
    productos.stock = stock
    productos.imagen = imagen
    productos.save()
    
    return redirect('/')
       

def eliminarProducto(request, codigo):
    productos = Producto.objects.get(codigo=codigo)
    productos.delete()
    return redirect('homeAdmin')

def registrarDescuento(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    porcentaje=request.POST['porcentaje']

    descuento = Descuento.objects.create(id=id, nombre=nombre, porcentaje=porcentaje)
    return redirect('homeAdmin')

def actualizarDescuento(request, id):
    descuento = Descuento.objects.get(id=id)
    return render(request, 'core/actualizar_descuento.html', {'descuento':descuento})

def editarDescuento(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    porcentaje=request.POST['porcentaje']
    
    descuento = Descuento.objects.get(id=id)
    descuento.nombre = nombre
    descuento.porcentaje = porcentaje
    descuento.save()
    
    return redirect('homeAdmin')

def eliminarDescuento(request, id):
    descuento = Descuento.objects.get(id=id)
    descuento.delete()
    return redirect('homeAdmin')

def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('/')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'core/registro.html', context)
# def registro(request):
#     if request.method == 'POST':
#         #estructura de condicion que verifica si el usuario que se intenta registrar existe
#         if Usuario.objects.filter(email = request.POST['correo']).exists(): # se verifica la existencia por el campo de email
#             messages.success(request, 'El usuario ingresado ya existe')
#         else:
#             #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html

#             nombre = request.POST['nombre'],
#             apellido = request.POST['apellido'],
#             email = request.POST['correo'],
#             ciudad = request.POST['ciudad'],
#             pwd = request.POST['password']
        
#             #se guarda el nuevo usuario en la base de datos
#             usuario = Usuario.objects.create(nombre=nombre, apellido=apellido, email=email, ciudad=ciudad, pwd=pwd)
#             usuario.save()
#             messages.success(request, 'Usuario registrado correctamente')
#             return redirect('login')
#     return render(request, 'core/registro.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo=producto_id)
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
        carrito.agregar(producto) 
    return redirect("carro")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo=producto_id)
    carrito.eliminar(producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo=producto_id)
    if producto.stock >= 0:
        producto.stock += 1
        producto.save()
        carrito.restar(producto)
    return redirect("carro")

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carro")

def comprar(request, precio):
    codigo = 0
    codigo = precio *99/234
    newHistorial = Historial.objects.create( codigo =codigo  , precio = precio ,fecha = datetime.now() )
    for key, value in request.session["carrito"].items():
        carrito = Carrito(request)
        carrito.limpiar()

    return redirect('carro')

 