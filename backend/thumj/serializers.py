from rest_framework import serializers
from .models import Paipu, Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class PaipuSerializer(serializers.ModelSerializer):
    
    score_list = serializers.JSONField()
    
    class Meta:
        model = Paipu
        fields = ['id', 'ref', 'log', 'ratingc', 'rule', 'lobby', 'dan', 'rate', 'sx', 'name', 'title', 'sc', 'score_list']
        