from django.shortcuts import render
from rest_framework import viewsets
from .models import Timeline
from .serializer import TimelineSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class TimelineViewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Timeline.objects.all()
        id_user = self.request.query_params.get('iduser',None)
        if id_user:
            queryset = queryset.filter(iduser=id_user)
        serializers = TimelineSerializer(queryset, many=True)
        return Response(serializers.data)