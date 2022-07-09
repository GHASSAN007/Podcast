from django.contrib import admin
from .models import *


def change_lang_to_ENGLISH(modleadmin , request , queryset):
    queryset.update(language = 'EN')



@admin.register(Podcast_info)
class  podcastInfo(admin.ModelAdmin):
    list_display = ['id','Title', 'Description' , 'podcast', 'Thumbnail', 'posting_date', 'channel' , 'is_viewed' , 'is_liked' , 'likes' , 'views', 'language', 'is_podcast_blocked']
    actions = [change_lang_to_ENGLISH]

@admin.register(comment)

class  Comments(admin.ModelAdmin):
    list_display = ['text','date_of_comment', 'podcast','user','is_podcast_comment_blocked']
