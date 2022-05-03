from django.urls import path
from .views import index, loginPage

urlpatterns = [
    path('', index),
    path('login/', index)
]