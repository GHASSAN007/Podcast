from django.db import models


class channel(models.Model):
	
	id = models.AutoField(primary_key=True)
	channel_name = models.CharField(max_length=250 , unique=True) 
	storyteller = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
	subscribers = models.PositiveIntegerField(default=0)
	creation_date  = models.DateField(auto_now=True)
	podcast_num = models.PositiveIntegerField(default=0)
	is_story_channel_blocked = models.BooleanField(default=False)

	def __string__(self):
		return self.channel_name
