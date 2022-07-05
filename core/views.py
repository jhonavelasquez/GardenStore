from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *



def home(request):
    contexto = {'producto': Producto.objects.all()}
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
    return render(request, 'core/historial.html')

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

def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email 
            contexto = Producto.objects.all()
            return redirect('home')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'core/login.html')

def loginAdmin(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email 
            contexto = Producto.objects.all()
            return redirect('homeAdmin')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Correo o constraseña no son correctos')
    return render(request, 'core/login.html')

def registro(request):
    if request.method == 'POST':
        #estructura de condicion que verifica si el usuario que se intenta registrar existe
        if Usuario.objects.filter(email = request.POST['correo']).exists(): # se verifica la existencia por el campo de email
            messages.success(request, 'El usuario ingresado ya existe')
        else:
            #creacion del nuevo usuario, entre [] se coloca el atributo "name" de los input en el html

            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            email = request.POST['correo'],
            ciudad = request.POST['ciudad'],
            pwd = request.POST['password']
        
            #se guarda el nuevo usuario en la base de datos
            usuario = Usuario.objects.create(nombre=nombre, apellido=apellido, email=email, ciudad=ciudad, pwd=pwd)
            usuario.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('login')
    return render(request, 'core/registro.html')