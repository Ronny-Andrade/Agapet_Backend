from .views import TimelineViewSet
from django.urls import path


urlpatterns = [
    path('fases', TimelineViewSet.as_view()),
    
]
