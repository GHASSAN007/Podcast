from rest_framework import serializers
from .models import comment 

class comment_serializer(serializers.ModelSerializer):

    class Meta:
        model = comment
        fields = '__all__'
