from django.shortcuts import render
from rest_framework import viewsets
from .models import Vacuna
from .serializer import VacunaSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class VacunasMascotaViewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Vacuna.objects.all()
        id_user = self.request.query_params.get('iduser',None)
        if id_user:
            queryset = queryset.filter(iduser=id_user)
        serializers = VacunaSerializer(queryset, many=True)
        return Response(serializers.data)
