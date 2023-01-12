from .views import VacunasMascotaViewSet
from django.urls import path


urlpatterns = [
    path('mascota/<str:pk>/', VacunasMascotaViewSet.as_view()),
    
]
