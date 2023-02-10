from rest_framework import serializers
from .models import Tema, Faq



class TemaSerializer(serializers.ModelSerializer):
    class Meta:
         model = Tema
         fields= '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
         model = Faq
         fields= '__all__'




