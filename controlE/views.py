#from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ClientesSerializers,EmpleadosSerializers,ReparacionesSerializers,AsignacionesSerializers
from .models import Clientes,Empleados,Reparaciones,Asignaciones

# Create your views here.

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers

class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializers

class ReparacionesViewSet(viewsets.ModelViewSet):
    queryset = Reparaciones.objects.all()
    serializer_class = ReparacionesSerializers

class AsignacionesViewSet(viewsets.ModelViewSet):
    queryset = Asignaciones.objects.all()
    serializer_class = AsignacionesSerializers
