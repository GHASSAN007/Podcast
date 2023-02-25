from rest_framework import serializers
from .models import location

class location_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = location
        fields = '__all__'
