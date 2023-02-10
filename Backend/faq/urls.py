from .views import FaqTemaViewSet, TemaList, FaqList
from django.urls import path

urlpatterns = [
    path('tema', TemaList.as_view()),
    path('faq', FaqList.as_view()),
    path('faq/tema', FaqTemaViewSet.as_view()),
    
]
