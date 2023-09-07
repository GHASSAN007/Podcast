from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('podcast_api/' , include('Podcast.urls')),
    path('stories_api/' , include('stores.urls')),
    path('comments_api/', include('Comments.urls')),
    path('channels_api/', include('Channels.urls')),
    path('location/', include('Geo_Location.urls')),
    path('', include('Front_end.urls'))

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
