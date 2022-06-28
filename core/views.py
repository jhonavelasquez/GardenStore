from django.shortcuts import render, redirect
from .forms import VehiculoForm, RegistroForm
from .models import *

# Create your views here.
def home(request):
    contexto = {'vehiculos': Vehiculo.objects.all()}
    return render(request, 'core/home.html', contexto)

def crearVehiculo(request):
    datos = {"form":VehiculoForm()}
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo agregado!."
    return render(request, 'core/crearVehiculo.html', datos)

def modificarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {"form":VehiculoForm(instance=vehiculo)}
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Vehiculo modificado!."
            datos['form'] = form
    return render(request, 'core/modificarVehiculo.html', datos)

def eliminarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to='home')

def registro(request):    
    if request.method == 'POST':
        form =RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    else: 
        form = RegistroForm()      
        return render(request, 'core/registro.html', {'form':form})