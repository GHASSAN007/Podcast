from rest_framework import serializers
from .models import stores_info 

class storesSerializer(serializers.ModelSerializer):

    class Meta:
        model = stores_info
        fields = '__all__'

