from rest_framework import serializers
from .models import Paipu, Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class PaipuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paipu
        fields = '__all__'