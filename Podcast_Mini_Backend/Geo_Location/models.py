from ipaddress import ip_address
from django.db import models
from django.contrib.auth.models import User

class location(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ip = models.CharField(max_length=255)
    latitude = models.FloatField(null=True , blank=True) 
    longitude = models.FloatField(null=True , blank=True)