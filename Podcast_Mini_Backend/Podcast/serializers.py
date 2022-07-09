from rest_framework import serializers
from .models import *

class Podcast_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast_info
        fields = '__all__'

    
class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model = comment
        fields = '__all__'



