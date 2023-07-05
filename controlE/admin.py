from django.contrib import admin

# Register your models here.
#para ver el modelo creado controlE.model

from .models import Clientes,Empleados,Reparaciones,Asignaciones

admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Reparaciones)
admin.site.register(Asignaciones)

