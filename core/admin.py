from atexit import register
from django.contrib import admin

from core.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Descuento)
admin.site.register(Historial)