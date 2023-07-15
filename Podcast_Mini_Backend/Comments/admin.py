from django.contrib import admin
from .models import comment


@admin.register(comment)

class  Comments(admin.ModelAdmin):
    list_display = ['id','text','date_of_comment','user','is_podcast_comment_blocked']

# Register your models here.
