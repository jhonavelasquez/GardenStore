from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto,Usuario

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

def login(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(email = request.POST['email'], pwd = request.POST['password'])
            request.session['email'] = newUser.email 
            contexto = Producto.objects.all()
            return redirect('tienda')
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
            newUser = Usuario(
                rut = request.POST['rut'],
                nombre = request.POST['nombre'],
                apellido = request.POST['apellido'],
                email = request.POST['correo'],
                pwd = request.POST['password']
            )
            # Carrito(username = request.POST['correo'], subtotal = 0).save()
            #se guarda el nuevo usuario en la base de datos
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
    return render(request, 'core/registro.html')

