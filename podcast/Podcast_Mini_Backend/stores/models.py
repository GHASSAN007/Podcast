from django.db import models
from Podcast.models import  Languages

class stores(models.Model):

    title : str = models.CharField(max_length = 200, unique=True)                   # Main Title of story
    suptitle : str = models.TextField(default = title )                             #subtitle of each story
    storys = models.FileField(upload_to = 'stores_audio/')                             # the audio file  
    Thumbnail = models.ImageField(upload_to = 'stores_Thumbnail/')                         #the image of podcast
    posting_date  = models.DateTimeField(auto_now=True)
    podcasted_by : str = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    channels = models.ForeignKey('story_channels' , on_delete=models.CASCADE ) 
    comments = models.ForeignKey('story_comments' , on_delete=models.CASCADE ,blank=True , null=True)
    is_listened : bool = models.BooleanField(default = False)                       # checking if the user listend to the story  
    is_liked : bool = models.BooleanField(default = False)                          # checking if the user liked the story before 
    likes  : int = models.IntegerField( default=0 )                                 # number of likes 
    listened : int = models.IntegerField(default=0)                                 # number of playing 
    language : str = models.CharField(max_length=3, choices=Languages)
    is_locked : bool = models.BooleanField(default=False)


    def __string__(self):
        return self.title




class story_channels(models.Model):
	channel_name : str = models.CharField(max_length=250 , unique=True)            
	storer = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
	subscribers : int = models.IntegerField(default=False)
	creation_date  = models.DateField(auto_now=True)
	podcast_num : int = models.IntegerField(default=0)

	def __string__(self):
		return self.channel_name


class story_comments(models.Model):
    text : str = models.TextField(blank=False)
    date_of_comment = models.DateTimeField(auto_now=True)
    story = models.ForeignKey(stores , on_delete = models.CASCADE)
    user = models.ForeignKey('auth.User' , on_delete = models.CASCADE)

    def __string__(self):
        return self.text
