from django.db import models

from Podcast.models import podcast

class comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=False)
    date_of_comment = models.DateTimeField(auto_now=True)
    podcast = models.ForeignKey('Podcast.Podcast', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    is_podcast_comment_blocked = models.BooleanField(default=False)

    def __string__(self):
        return self.text
