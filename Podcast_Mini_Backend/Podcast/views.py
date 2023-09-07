from rest_framework import status
from django.http import HttpResponseNotAllowed

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import podcast_serializer 
from .models import *


class api_over_view(APIView):
    def get(request):
        api_urls = {
            'List_podcast':'/podcast-list/',               
            'Podcast_Detailview':'/podcast-view/<str:pk>',
            'Create_podcast':'/create-podcast/',
            'Update-podcast': '/podcast-update/<str:pk>/',
            'Delete_podcast': '/podcast-delete/<str:pk>/',
        }

        return Response(api_urls)

class podcast_list(APIView):
    def get(request):
        podcasts = podcast.objects.all()
        serializer = podcast_serializer(podcasts , many=True)
        return Response(serializer.data)

class podcast_detail(APIView):
    def get(request , pk):
        podcast = podcast.objects.get(pk=pk)
        if podcast.is_podcast_blocked:
            return HttpResponseNotAllowed            
        else:
            serializer = podcast_serializer(podcast , many=False)

            return Response(serializer.data)


class podcast_create(APIView):
    def post(self, request):
        serializer = podcast_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

class podcast_update(APIView):
    def podcast_update(request , pk):
        podcast = podcast.objects.get(pk=pk)
        serializer = podcast_serializer(instance=podcast, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
class podcast_delete(APIView):
    def delete_podcast(request, pk):
        podcast = podcast.objects.get(pk=pk)
        podcast.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------