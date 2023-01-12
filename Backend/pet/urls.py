from .views import MascotaViewSet, UsuarioMascotaViewSet
from rest_framework import routers
from django.urls import path


router_mascota = routers.DefaultRouter()
router_mascota.register(prefix='mascota', basename='mascota', viewset=MascotaViewSet)

urlpatterns = [
    path('usuario/<str:pk>/', UsuarioMascotaViewSet.as_view()),
    
]
