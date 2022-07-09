from rest_framework import serializers
from .models import *

class storesSerializer(serializers.ModelSerializer):

    class Meta:
        model = stores_info
        fields = '__all__'

   
class story_commentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = story_comments
        fields = '__all__'


