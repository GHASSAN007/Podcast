from django.db import models
from django.contrib.auth.models import User

class location(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    location = models.TextField()
        