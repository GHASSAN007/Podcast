from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.apiOverview , name='api_overview'),
    
    path('stories-list/' , views.List_stories , name="stores_list"),
    path('story-view/<str:pk>/' , views.story_detail , name="story_detail"),
    path('create-story/' , views.Create_story , name="create_story"),
    path('story-update/<str:pk>' , views.Update_story , name= "update_story"),
    path('story-delete/<str:pk>' , views.Delete_story ,name="delete_story"),
]