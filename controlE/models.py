from django.db import models

# Create your models here.

class Clientes(models.Model):
  nombre = models.CharField(max_length=30)
  direccion = models.CharField(max_length=50)
  telefono = models.CharField(max_length=15)
  email = models.EmailField()

class Empleados(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email= models.EmailField()

class Reparaciones(models.Model):
    cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    equipo = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=200)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
  
class Asignaciones(models.Model):
  reparacion_id = models.ForeignKey(Reparaciones, on_delete=models.CASCADE)
  empleado_id = models.ForeignKey(Empleados, on_delete=models.CASCADE)
  fecha_asignacion=  models.DateTimeField(auto_now_add=True)
