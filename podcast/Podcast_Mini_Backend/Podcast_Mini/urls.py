from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from Podcast.models import Podcast_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('podcast_api/' , include('Podcast.urls')),
    path('stories_api/' , include('stores.urls')),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
