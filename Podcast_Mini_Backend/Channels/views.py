from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import channel

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List_stories_channels':'/channels-list/',
        'stories_channels_Detailview':'channels-view/<str:pk>',
        'Create_stories_channels':'/create-channel/',
        'Update-stories_channels': '/channel-update/<str:pk>/',
        'Delete_stories_channels': '/channels-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def stories_channels_List(request):
    _channels = story_channels.objects.all()
    serializer = story_channelsSerializer(_channels , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stories_channels_detail(request , pk):
    _channel = story_channels.objects.get(pk=pk)
    serializer = story_channelsSerializer(_channel , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_stories_channels(request):
    serializer = story_channelsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update_stories_channels(request , pk):
    _channel = story_channels.objects.get(pk=pk)
    serializer = story_channelsSerializer( instance=_channel, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_stories_channels(request, pk):
    _channel = story_channels.objects.get(pk=pk)
    _channel.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
