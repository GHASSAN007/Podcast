from django.contrib import admin
from .models import channel


@admin.register(channel)
class Channels(admin.ModelAdmin):
    list_display = ['channel_name', 'storyteller',
                    'subscribers', 'creation_date', 'podcast_num']

