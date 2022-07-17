from django.contrib import admin
from .models import podcast


def change_lang_to_ENGLISH(modleadmin , request , queryset):
    queryset.update(language = 'EN')

@admin.register(podcast)
class  podcastInfo(admin.ModelAdmin):
    list_display = ['id','Title', 'Description' , 'podcast', 'Thumbnail', 'posting_date', 'channel' , 'is_viewed' , 'is_liked' , 'likes' , 'views', 'language', 'is_podcast_blocked']
    actions = [change_lang_to_ENGLISH]
