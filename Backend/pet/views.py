from django.shortcuts import render
from rest_framework import viewsets
from .models import Animal, Mascota
from .serializer import AnimalSerializer, MascotaSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MascotaViewSet(viewsets.ModelViewSet):
    serializer_class = MascotaSerializer
    queryset = Mascota.objects.all()

class UsuarioMascotaViewSet(APIView):
    def get(self, request,pk):
        user = Mascota.objects.get(iduser=pk)
        serializers = MascotaSerializer(user, many=False)
        return Response(serializers.data)