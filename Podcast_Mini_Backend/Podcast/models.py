from django.db import models
from django.contrib import auth
from django.core.exceptions import ValidationError

from Scripts import validate_podcast_extension, validate_thumbnail_extension, Languages

# class for podcast data

from Channels.models import channel
class Podcast_info(models.Model):

    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200, unique=True)
    Description = models.TextField()
    podcast = models.FileField(upload_to='podcasts/',  validators=[validate_podcast_extension])
    Thumbnail = models.ImageField( upload_to='Thumbnail/', validators=[validate_thumbnail_extension])
    posting_date = models.DateTimeField(auto_now=True)
    podcasted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    channel = models.ForeignKey('Channels.channel', on_delete=models.CASCADE)
    is_viewed = models.BooleanField(default=False)
    is_liked = models.BooleanField(default=False)
    likes = models.PositiveIntegerField(default=0) 
    views = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=3, choices=Languages)
    is_podcast_blocked = models.BooleanField(default=False)
    is_private_podcast = models.BooleanField(default=False)

    def __string__(self):
        return self.Title


class comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=False)
    date_of_comment = models.DateTimeField(auto_now=True)
    podcast = models.ForeignKey(Podcast_info, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    is_podcast_comment_blocked = models.BooleanField(default=False)

    def __string__(self):
        return self.text


