from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_over_view.as_view() , name='api_over_view'),
    
    path('podcast-list/' , views.podcast_list.as_view() , name="podcast_list"),
    path('podcast-view/<str:pk>/' , views.podcast_detail.as_view(), name="podcast_detail"),
    path('create-podcast/' , views.podcast_create.as_view(), name="create_podcast"),
    path('podcast-update/<str:pk>' , views.podcast_update.as_view() , name= "update_podcast"),
    path('podcast-delete/<str:pk>' , views.podcast_delete.as_view() ,name="delete_podcast"),
]