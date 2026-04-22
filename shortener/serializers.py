from rest_framework import serializers
from .models import URL

class ShortenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(source='longurl')
    shortCode = serializers.CharField(source='shorturl', read_only=True)

    class Meta:
        model = URL
        fields = ['id', 'url', 'shortCode', 'created_at', 'updated_at','access_count']
        read_only_fields = ['shortCode', 'created_at', 'updated_at', 'access_count']