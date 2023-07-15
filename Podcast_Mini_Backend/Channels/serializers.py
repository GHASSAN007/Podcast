from rest_framework import serializers
from .models import channel


class story_channelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = channel
        fields = '__all__'

    
