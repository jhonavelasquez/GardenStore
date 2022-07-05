from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('homeAdmin', homeAdmin, name='homeAdmin'),
    path('crudProducto', crudProducto, name="crudProducto"),
    path('crudDescuento', crudDescuento, name="crudDescuento"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('loginAdmin', LoginView.as_view(template_name="core/login.html"), name="loginAdmin"),
    path('registro', registro, name="registro"),
    path('historial', historial, name='historial'),
    path('suscripcion', suscripcion, name='suscripcion'),
    path('carro', carro, name='carro'),
    path('carrito', carrito, name='carrito'),
    path('agregarproducto/<user_id>/<prod_id>', agregarProducto, name='add'),   
    path('comprar/<p_total>/<id_carrito>', comprar, name='comprar'),
    path('multicompra/<prod_id>/<user_id>', multiCompra, name="multicompra"),
    

    #funciones del crud
    path('registrarProducto/', registrarProducto),
    path('actualizarProducto/<codigo>', actualizarProducto),
    path('eliminarProducto/<codigo>', eliminarProducto),
    path('editarProducto/', editarProducto),

    path('registrarDescuento/', registrarDescuento),
    path('actualizarDescuento/<id>', actualizarDescuento),
    path('eliminarDescuento/<id>', eliminarDescuento),
    path('editarDescuento/', editarDescuento),
]

