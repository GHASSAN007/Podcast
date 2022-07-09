from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview , name='api_overview'),
    #------------------------------------------------------------------------------
    path('podcast-list/' , views.podcast_List , name="podcast_list"),
    path('podcast-view/<str:pk>/' , views.Podcast_detail , name="podcast_detail"),
    path('create-podcast/' , views.podcast_create , name="create_podcast"),
    path('podcast-update/<str:pk>' , views.podcast_update , name= "update_podcast"),
    path('podcast-delete/<str:pk>' , views.delete_podcast ,name="delete_podcast"),
    #------------------------------------------------------------------------------
    path('comments-list/' , views.comments_List , name="comment_list"),
    path('comment-view/<str:pk>/' , views.comment_detail , name="comment_detail"),
    path('create-comment/' , views.comment_create , name="create_comment"),
    path('comment-update/<str:pk>' , views.comment_update , name= "update_comment"),
    path('comment-delete/<str:pk>' , views.Delete_comment ,name="delete_comment"),
    #------------------------------------------------------------------------------

]