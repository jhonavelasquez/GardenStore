from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('crearVehiculo', crearVehiculo, name="crearVehiculo"),
    path('modificarVehiculo/<id>', modificarVehiculo, name="modificarVehiculo"),
    path('eliminarVehiculo/<id>', eliminarVehiculo, name="eliminarVehiculo"),
    path('login', LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout', LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path('registro', registro, name="registro"),
]
