from django.shortcuts import render
from rest_framework import viewsets
from .models import Vacuna, Vacuna_Mascota
from .serializer import VacunaMascotaSerializer, VacunaSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class VacunasMascotaViewSet(APIView):
    def get(self, request,pk):
        vacuna_mascota = Vacuna_Mascota.objects.get(idpet=pk)
        serializers = VacunaMascotaSerializer(vacuna_mascota, many=False)
        return Response(serializers.data)