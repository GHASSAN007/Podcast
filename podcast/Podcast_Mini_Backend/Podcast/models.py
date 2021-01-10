from django.db import models
from django.contrib import auth


ENGLISH = 'EN'
ARABIC = 'AR'
CHINES = 'ZH'
DUTCH = 'NL'
FRENCH = 'FR'
GERMAN = 'DE'
RUSSIAN = 'RU'
JAPANESE = 'JA'

Languages = [
    (ENGLISH, 'English'),
    (ARABIC, 'Arabic'),
    (CHINES, 'Chines'),
    (DUTCH, 'Dutch'),
    (FRENCH, 'French'),
    (GERMAN, 'German'),
    (RUSSIAN, 'Russian'),
    (JAPANESE, 'Japanese'),
]

#class for podcast data 
class Podcast_info(models.Model):
    
    Title : str = models.CharField(max_length = 200, unique=True)                                # Title of the podcast
    Description : str = models.TextField(blank = True , default = "No Description") #description of each podcast / story
    podcast = models.FileField(upload_to = 'podcasts/')                             # the audio file  
    Thumbnail = models.ImageField(upload_to = 'Thumbnail/')                         #the image of podcast
    posting_date  = models.DateTimeField(auto_now=True)
    podcasted_by : str = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    channel = models.ForeignKey('channel' , on_delete=models.CASCADE ) 
    is_viewed : bool = models.BooleanField(default = False)                         # checking if the user listend to the podcast beviewed 
    is_liked : bool = models.BooleanField(default = False)                          # checking if the user liked the podcast before 
    likes  : int = models.IntegerField( default=0 )                                 #number of likes 
    views : int = models.IntegerField(default=0)                                    # number of views 
    language : str = models.CharField(max_length=3, choices=Languages)

    def __string__(self):
        return self.Title




class channel(models.Model):
	channel_name : str = models.CharField(max_length=250 , unique=True)            
	podcast_maker = models.ForeignKey('auth.User' , on_delete=models.CASCADE)
	subscribers : int = models.IntegerField(default=False)
	creation_date  = models.DateField(auto_now=True)
	podcast_num : int = models.IntegerField(default=0)

	def __string__(self):
		return self.channel_name


class comment(models.Model):
    text : str = models.TextField(blank=False)
    date_of_comment = models.DateTimeField(auto_now=True)
    podcast = models.ForeignKey(Podcast_info , on_delete = models.CASCADE)
    user = models.ForeignKey('auth.User' , on_delete = models.CASCADE)

    def __string__(self):
        return self.text

