from django.contrib import admin
from .models import story 


@admin.register(story)
class Stores(admin.ModelAdmin):
    list_display = ['id','title', 'suptitle', 'stores', 'Thumbnail', 'posting_date',
                    'podcasted_by', 'channels', 'likes', 'listened', 'language']


