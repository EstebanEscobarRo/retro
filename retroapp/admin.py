from django.contrib import admin

# Register your models here.

from . models import Juego, Genero, Empresa, JuegoInstance

admin.site.register(Juego)
admin.site.register(Genero)
admin.site.register(Empresa)
admin.site.register(JuegoInstance)