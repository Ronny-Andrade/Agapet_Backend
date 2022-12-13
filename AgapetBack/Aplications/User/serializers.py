from rest_framework import serializers
from .models import User, Rol_User

# Serializer from model user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

    
    def create(self, validated_data):
        return User.objects.create(**validated_data)


# Serializer from model rol_user       
class Rol_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_User
        fields = '__all__'