from django.db import models
from django.contrib import auth
#from .channel.models import channel, Podcaster_info
#from .comments import comment

"""
=============================================
=        podcast info and podcast           =
=                                           =
=                                           =
=                                           =
=                                           =
=============================================
"""


#class for podcast data 
class Podcast_info(models.Model):
    # add Podcaster_info
    Thumbnail :  models.ImageField(upload_to='Thumbnail/')
    Title : str = models.CharField(max_length=200) # Title of the podcast
    Description : str = models.TextField(blank=True , default="No Description")
    #add Comments
    is_viewed : bool = models.BooleanField(default=False)
    is_liked : bool = models.BooleanField(default=False)
    podcast = models.FileField(upload_to ='podcasts/') 

    def __string__(self):
        return self.Title  
    

    
