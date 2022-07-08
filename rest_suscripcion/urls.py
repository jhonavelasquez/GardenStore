from django.urls import path
from rest_suscripcion.views import datalle_suscripcion, lista_suscripcion

urlpatterns =[
    path('lista_suscripcion', lista_suscripcion, name="lista_suscripcion"),
    path('datalle_suscripcion/<id>', datalle_suscripcion, name="datalle_suscripcion"),
]