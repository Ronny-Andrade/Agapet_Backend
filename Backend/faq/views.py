from django.shortcuts import render
from rest_framework import viewsets
from .models import Tema, Faq
from .serializer import TemaSerializer, FaqSerializer
# otras importaciones
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class TemaList(APIView):
    def get(self, request):
        tema = Tema.objects.all()
        serializer = TemaSerializer(tema, many=True)
        return Response(serializer.data)

class FaqList(APIView):
    def get(self, request):
        faq = Faq.objects.all()
        serializer = FaqSerializer(faq, many=True)
        return Response(serializer.data)

class FaqTemaViewSet(APIView):
    def get(self, request,*args,**kwargs):
        queryset = Faq.objects.all()
        temaid = self.request.query_params.get('temaid',None)
        if temaid:
            queryset = queryset.filter(temaid=temaid)
        serializers = FaqSerializer(queryset, many=True)
        return Response(serializers.data)