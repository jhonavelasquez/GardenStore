from django.urls import path
from .views import *

# urlpatterns = [
#     path('', home, name="home"),
#     path('crearVehiculo', crearVehiculo, name="crearVehiculo"),
#     path('modificarVehiculo/<id>', modificarVehiculo, name="modificarVehiculo"),
#     path('eliminarVehiculo/<id>', eliminarVehiculo, name="eliminarVehiculo"),
#     path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
#     path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
#     path('registro', registro, name="registro"),
# ]


# ejemplo de url falta terminar 

urlpatterns = [
    path('', home, name='home'),
    path('registrarProducto/', registrarProducto),
    path('actualizarProducto/<codigo>', actualizarProducto),
    path('eliminarProducto/<codigo>', eliminarProducto)
    
    # path('', Login, name='login'),
    # path('registro', registro, name='registro'),
    # path('tienda', tienda, name="tienda"),  
    # path('producto/<prod_id>', producto, name='producto'),
    # path('arriendo-form', arr_form, name='arriendo-form'),
    # path('mantencion-form', mant_form, name="mantencion-form"),
    # path('agregarproducto/<user_id>/<prod_id>', agregarProducto, name='add'),   
    # path('carrito', carrito, name='carrito'),
    # path('comprar/<p_total>/<id_carrito>', comprar, name='comprar'),
    # path('multicompra/<prod_id>/<user_id>', multiCompra, name="multicompra"),
    # path('home', home, name='home'),
    # path('historial', historial, name='historial'),
]