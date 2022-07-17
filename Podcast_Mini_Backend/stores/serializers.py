from rest_framework import serializers
from .models import story 

class story_serializer(serializers.ModelSerializer):

    class Meta:
        model = story
        fields = '__all__'

