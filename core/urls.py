from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('homeAdmin', homeAdmin, name='homeAdmin'),
    path('crudProducto', crudProducto, name="crudProducto"),
    path('crudDescuento', crudDescuento, name="crudDescuento"),
    path('', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('registro', registro, name="registro"),
    path('historial', historial, name='historial'),
    path('suscripcion', suscripcion, name='suscripcion'),
    path('carro', carro, name='carro'),

    #funciones del crud
    path('registrarProducto/', registrarProducto),
    path('actualizarProducto/<codigo>', actualizarProducto),
    path('eliminarProducto/<codigo>', eliminarProducto),
    path('editarProducto/', editarProducto),

    path('registrarDescuento/', registrarDescuento),
    path('actualizarDescuento/<id>', actualizarDescuento),
    path('eliminarDescuento/<id>', eliminarDescuento),
    path('editarDescuento/', editarDescuento),

    #funciones del carrito
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_producto, name="cls"),
    path('comprar/<int:precio>', comprar, name="comprar"),
]