from rest_framework import serializers
from .models import Animal, Mascota
from user.serializers import UserSerializer


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
         model = Animal
         fields= '__all__'

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Mascota
         fields= '__all__'




