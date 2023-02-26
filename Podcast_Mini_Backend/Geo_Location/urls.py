from django.urls import path
from . import views

urlpatterns=[
    path('location-list/', views.location_List, name="LocationList" ),
    path('location-add/', views.get_ip , name="LocationAdd"),
    path('delete/', views.delete , name="test")
]