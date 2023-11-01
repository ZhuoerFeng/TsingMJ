from rest_framework import serializers
from .models import Paipu, Test

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class PaipuSerializer(serializers.ModelSerializer):
    
    score_list = serializers.JSONField(read_only=True)
    
    class Meta:
        model = Paipu
        fields = ['id', 'ref', 'ratingc', 'log', 'rule', 'lobby', 'dan', 'rate', 'sx', 'name', 'title', 'sc', 'score_list', "match_name"]
        