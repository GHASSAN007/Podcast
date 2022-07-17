from django.db import models

from Scripts import validate_podcast_extension, validate_thumbnail_extension, Languages
from Channels.models import channel
from Comments.models import comment
class story(models.Model):

	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 200, unique=True)# Main Title of story
	suptitle = models.TextField()#subtitle of each story
	stores = models.FileField(upload_to = 'stores_audio/',  validators=[validate_podcast_extension])# the audio file  
	Thumbnail = models.ImageField(upload_to = 'stores_Thumbnail/' , validators=[validate_thumbnail_extension])#the image of podcast
	posting_date = models.DateTimeField(auto_now=True)
	podcasted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	channels = models.ForeignKey('Channels.channel' , on_delete=models.CASCADE ) 
	comments = models.ForeignKey('Comments.comment' , on_delete=models.CASCADE ,blank=True , null=True)
	is_listened = models.BooleanField(default = False)# checking if the user listend to the story  
	is_liked = models.BooleanField(default = False)# checking if the user liked the story before 
	likes = models.PositiveIntegerField(default=0 )# number of likes 
	listened = models.PositiveIntegerField(default=0)  # number of playing 
	language = models.CharField(max_length=3, choices=Languages)
	is_stores_blocked = models.BooleanField(default=False)
	is_private_story = models.BooleanField(default=False)

	def __string__(self):
		return self.title

