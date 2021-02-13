from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('podcast_api/' , include('Podcast.urls')),
    path('stories_api/' , include('stores.urls')),
]
