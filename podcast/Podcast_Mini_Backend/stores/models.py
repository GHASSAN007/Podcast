from django.db import models
from Podcast.models import  Languages
from CODE_FOR_APPS.validators import validate_podcast_extension, validate_thumbnail_extension

class stores(models.Model):

    title = models.CharField(max_length = 200, unique=True)# Main Title of story
    suptitle = models.TextField(default = title )#subtitle of each story
    storys = models.FileField(upload_to = 'stores_audio/',  validators=[validate_podcast_extension])# the audio file  
    Thumbnail = models.ImageField(upload_to = 'stores_Thumbnail/' , validators=[validate_thumbnail_extension])#the image of podcast
    posting_date = models.DateTimeField(auto_now=True)
    podcasted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    channels = models.ForeignKey('story_channels' , on_delete=models.CASCADE ) 
    comments = models.ForeignKey('story_comments' , on_delete=models.CASCADE ,blank=True , null=True)
    is_listened = models.BooleanField(default = False)# checking if the user listend to the story  
    is_liked = models.BooleanField(default = False)# checking if the user liked the story before 
    likes = models.PositiveIntegerField(default=0 )# number of likes 
    listened = models.PositiveIntegerField(default=0)  # number of playing 
    language = models.CharField(max_length=3, choices=Languages)
    is_locked = models.BooleanField(default=False)


    def __string__(self):
        return self.title




class story_channels(models.Model):
	channel_name = models.CharField(max_length=250 , unique=True)            
	storer = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
	subscribers = models.PositiveIntegerField(default=0)
	creation_date  = models.DateField(auto_now=True)
	podcast_num = models.PositiveIntegerField(default=0)

	def __string__(self):
		return self.channel_name


class story_comments(models.Model):
    text = models.TextField(blank=False)
    date_of_comment = models.DateTimeField(auto_now=True)
    story = models.ForeignKey(stores , on_delete = models.CASCADE)
    user = models.ForeignKey('auth.User' , on_delete = models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    
    def __string__(self):
        return self.text
