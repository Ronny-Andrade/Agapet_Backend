from rest_framework import serializers
from .models import Vacuna

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna
         fields= '__all__'


class VacunaUpdateSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna
         fields= ['lugar_vacuna','fecha','imagen64','descripcion_vacuna']
