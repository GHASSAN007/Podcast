from django.urls import path
from . import views

urlpatterns = [
    path('comments-list/' , views.comments_List , name="comment_list"),
    path('comment-view/<str:pk>/' , views.comment_detail , name="comment_detail"),
    path('create-comment/' , views.comment_create , name="create_comment"),
    path('comment-update/<str:pk>' , views.comment_update , name= "update_comment"),
    path('comment-delete/<str:pk>' , views.Delete_comment ,name="delete_comment"),

]