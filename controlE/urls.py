from django.urls import path,include
from rest_framework import routers
from controlE import views

router = routers.DefaultRouter()
router.register(r'cliente',views.ClientesViewSet)
router.register(r'empleado',views.EmpleadosViewSet)
router.register(r'reparaciones',views.ReparacionesViewSet)
router.register(r'asignaciones',views.AsignacionesViewSet)

urlpatterns = [
    path('',include(router.urls))
]
