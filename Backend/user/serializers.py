from rest_framework import serializers
from .models import User

# Serializer from model user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser','name','email','phone','direction', 'age','points','image']
        

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['iduser','name','email','password','phone','direction']
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        
