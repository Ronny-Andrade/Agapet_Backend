from django.shortcuts import render
from rest_framework import viewsets
from .models import Vacuna
from .serializer import VacunaSerializer, VacunaUpdateSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class VacunasMascotaViewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Vacuna.objects.all()
        id_user = self.request.query_params.get('iduser',None)
        if id_user:
            queryset = queryset.filter(iduser=id_user)
        serializers = VacunaSerializer(queryset, many=True)
        return Response(serializers.data)

class Mascotaupdate(APIView):
    def put(self, request, pk):
        vacuna = Vacuna.objects.get(vacuna_id=pk)
        serializer = VacunaUpdateSerializer(instance=vacuna, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


