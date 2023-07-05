from rest_framework import serializers
from .models import Clientes,Empleados,Reparaciones,Asignaciones

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fileds = '__all__'

class EmpleadosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = '__all__'

class ReparacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reparaciones
        fields = '__all__'

class AsignacionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignaciones
        fields = '__all__'

