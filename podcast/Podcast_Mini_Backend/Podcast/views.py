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
        # ------------------------------------------------  
        'List_podcast_info':'/podcast-list/',               
        'Podcast_Detailview':'/podcast-view/<str:pk>',
        'Create_podcast':'/create-podcast/',
        'Update-podcast': '/podcast-update/<str:pk>/',
        'Delete_podcast': '/podcast-delete/<str:pk>/',
        #-------------------------------------------------
        'List_channels':'/channels-list/',
        'channel_Detailview':'channel-view/<str:pk>',
        'Create_channel':'/create-channel/',
        'Update-channel': '/channel-update/<str:pk>/',
        'Delete_channel': '/channel-delete/<str:pk>/',
        #-------------------------------------------------
        'List_comments':'/comments-list/',
        'comment_Detailview':'comment-view/<str:pk>',
        'Create_comment':'/create-comment/',
        'Update-comment': '/comment-update/<str:pk>/',
        'Delete_comment': '/comment-delete/<str:pk>/',
        #-------------------------------------------------
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

 #-------------------------------------------------

@api_view(['GET'])
def channels_List(request):
    _channels = channel.objects.all()
    serializer = channelSerializer(_channels , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def channel_detail(request , pk):
    _channel = channel.objects.get(pk=pk)
    serializer = channelSerializer(_channel , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def channel_create(request):
    serializer = channelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def channel_update(request , pk):
    _channel = channel.objects.get(pk=pk)
    serializer = channelSerializer( instance=_channel, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_channel(request, pk):
    _channel = channel.objects.get(pk=pk)
    _channel.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------

@api_view(['GET'])
def comments_List(request):
    _comments = comment.objects.all()
    serializer = commentSerializer(_comments , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request , pk):
    _comment = comment.objects.get(pk=pk)
    serializer = commentSerializer(_comment , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request):
    serializer = commentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def comment_update(request , pk):
    _comment = comment.objects.get(pk=pk)
    serializer =commentSerializer( instance=_comment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_comment(request, pk):
    _comment = comment.objects.get(pk=pk)
    _comment.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------