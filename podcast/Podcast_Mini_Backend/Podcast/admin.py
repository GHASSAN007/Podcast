from django.contrib import admin
from .models import *

@admin.register(Podcast_info)

class  podcastInfo(admin.ModelAdmin):
    list_display = ['Title', 'Description' , 'podcast', 'Thumbnail', 'posting_date', 'channel' , 'is_viewed' , 'is_liked' , 'likes' , 'views', 'language']


@admin.register(channel)

class  Channels(admin.ModelAdmin):
    list_display = ['channel_name','podcast_maker', 'subscribers','creation_date', 'podcast_num']


@admin.register(comment)

class  Comments(admin.ModelAdmin):
    list_display = ['text','date_of_comment', 'podcast','user']