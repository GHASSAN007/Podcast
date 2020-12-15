from django.db import models
from django.contrib import auth
#from .channel.models import channel, Podcaster_info
#from .comments import comment



#class for podcast data 
class Podcast_info(models.Model):

    Title : str = models.CharField(max_length = 200)                                # Title of the podcast
    Description : str = models.TextField(blank = True , default = "No Description") #description of each podcast / story
    podcast = models.FileField(upload_to = 'podcasts/')                             # the audio file  
    Thumbnail = models.ImageField(upload_to = 'Thumbnail/')                        #the image of podcast
    podcasted_by : str = models.CharField(max_length=100)     
    is_viewed : bool = models.BooleanField(default = False)                         # checking if the user listend to the podcast before 
    is_liked : bool = models.BooleanField(default = False)                          # checking if the user liked the podcast before 
    likes  : int = models.IntegerField( default=0 )                                 #number of likes 
    views : int = models.IntegerField(default=0)                                    # number of views 
    #language : str = models.CharField()

    def __string__(self):
        return self.Title  
    
    
    
