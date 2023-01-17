from .views import VacunasMascotaViewSet, Mascotaupdate
from django.urls import path


urlpatterns = [
    path('mascota', VacunasMascotaViewSet.as_view()),
    path('actualizar/<str:pk>/', Mascotaupdate.as_view()),
    
]
