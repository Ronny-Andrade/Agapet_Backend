from .views import VacunasMascotaViewSet
from django.urls import path


urlpatterns = [
    path('mascota', VacunasMascotaViewSet.as_view()),
    
]
