from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Podcast_infoSerializer , channelSerializer , commentSerializer

from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List_podcast_info':'/podcast-list/',
        'Podcast_Detail_view':'/podcast-view/<str:pk>',
        'Create_podcast':'/create-podcast/',
        'Update-podcast': '/podcast-update/<str:pk>/',
        'Delete_podcast': '/podcast-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def podcast_List(request):
    podcasts = Podcast_info.objects.all()
    serializer = Podcast_infoSerializer(podcasts , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Podcast_detail(request , pk):
    podcast = Podcast_info.objects.get(pk=pk)
    serializer = Podcast_infoSerializer(podcast , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def podcast_create(request):
    serializer = Podcast_infoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def podcast_update(request , pk):
    podcast = Podcast_info.objects.get(pk=pk)
    serializer = Podcast_infoSerializer( instance=podcast, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_podcast(request, pk):
    podcast = Podcast_info.objects.get(pk=pk)
    podcast.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)