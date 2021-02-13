from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # ------------------------------------------------  
        'List_stories':'/stories-list/',               
        'story_Detailview':'/story-view/<str:pk>',
        'Create_story':'/create-story/',
        'Update_story': '/story-update/<str:pk>/',
        'Delete_story': '/story-delete/<str:pk>/',
        #-------------------------------------------------
        'List_stories_channels':'/channels-list/',
        'stories_channels_Detailview':'channels-view/<str:pk>',
        'Create_stories_channels':'/create-channel/',
        'Update-stories_channels': '/channel-update/<str:pk>/',
        'Delete_stories_channels': '/channels-delete/<str:pk>/',
        #-------------------------------------------------
        'List_story_comments':'/comments-list/',
        'story_comments_Detailview':'comment-view/<str:pk>',
        'Create_story_comments':'/create-comment/',
        'Update-story_comments': '/comment-update/<str:pk>/',
        'Delete_story_comments': '/comment-delete/<str:pk>/',
        #-------------------------------------------------
    }

    return Response(api_urls)

@api_view(['GET'])
def List_stories(request):
    stores = stores_info.objects.all()
    serializer = storesSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def story_detail(request , pk):
    story = stores_info.objects.get(pk=pk)
    serializer = storesSerializer(story, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def Create_story(request):
    serializer = storesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def Update_story(request , pk):
    story = stores_info.objects.get(pk=pk)
    serializer = storesSerializer( instance=story, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_story(request, pk):
    story = stores_info.objects.get(pk=pk)
    story.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------

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

 #-------------------------------------------------

@api_view(['GET'])
def story_comments_List(request):
    _comments = story_comments.objects.all()
    serializer = story_commentsSerializer(_comments , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def story_comments_detail(request , pk):
    _comment = story_comments.objects.get(pk=pk)
    serializer = story_commentsSerializer(_comment , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_story_comments(request):
    serializer = story_commentsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def update_story_comments(request , pk):
    _comment = story_comments.objects.get(pk=pk)
    serializer = story_commentsSerializer( instance=_comment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_story_comments(request, pk):
    _comment = story_comments.objects.get(pk=pk)
    _comment.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------