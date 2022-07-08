from rest_framework import serializers
from core.models import *

class SuscripcionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['nombre','fecha','descuento','monto']