from rest_framework import serializers
from .models import Daily

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily
        fields = ['id', 'date', 'study', 'research', 'hobby', 'others', 'future_work', 'evaluation', 'isOpen']
