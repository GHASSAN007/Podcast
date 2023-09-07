from django.urls import path
from . import views

urlpatterns=[
    path('', views.api_over_view.as_view(), name="api over view"),
    path('location-list/', views.location_list.as_view(), name="listting locations" ),
    path('location-add/', views.user_location.as_view() , name="location of the user"),
]