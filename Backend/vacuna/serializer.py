from rest_framework import serializers
from .models import Vacuna, Vacuna_Mascota

class VacunaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna
         fields= '__all__'
         
class VacunaMascotaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Vacuna_Mascota
         fields= '__all__'
        
