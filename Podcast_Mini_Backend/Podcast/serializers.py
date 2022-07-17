from rest_framework import serializers
from .models import podcast

class podcast_serializer(serializers.ModelSerializer):

    class Meta:
        model = podcast
        fields = '__all__'

    


