from django.contrib import admin
from .models import *


@admin.register(stores)
class Stores(admin.ModelAdmin):
    list_display = ['title', 'suptitle', 'stores', 'Thumbnail', 'posting_date',
                    'podcasted_by', 'channels', 'likes', 'listened', 'language']


@admin.register(story_channels)
class Story_Channels(admin.ModelAdmin):
    list_display = ['channel_name', 'storyteller',
                    'subscribers', 'creation_date', 'podcast_num']


@admin.register(story_comments)
class Comments(admin.ModelAdmin):
    list_display = ['text', 'date_of_comment', 'story', 'user']
