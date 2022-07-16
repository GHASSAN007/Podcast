from rest_framework import serializers
from .models import Podcast_info

class Podcast_infoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Podcast_info
        fields = '__all__'

    


