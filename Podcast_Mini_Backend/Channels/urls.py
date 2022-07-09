from django.urls import path
from . import views

urlpatterns = [
    path('channels-list/', views.stories_channels_List, name="channels_list"),
    path('channel-view/<str:pk>/',views.stories_channels_detail, name="channel_detail"),
    path('create-channel/', views.create_stories_channels,name="create_channel"),
    path('channel-update/<str:pk>',views.update_stories_channels, name="update_channel"),
    path('channel-delete/<str:pk>', views.Delete_stories_channels, name="delete_channel"), 
    ]
