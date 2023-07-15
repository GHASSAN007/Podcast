from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from django.http import HttpResponseNotAllowed , Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import podcast_serializer 
from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List_podcast':'/podcast-list/',               
        'Podcast_Detailview':'/podcast-view/<str:pk>',
        'Create_podcast':'/create-podcast/',
        'Update-podcast': '/podcast-update/<str:pk>/',
        'Delete_podcast': '/podcast-delete/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def podcast_List(request):
    podcasts = podcast.objects.all()
    serializer = podcast_serializer(podcasts , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Podcast_detail(request , pk):
#    if podcast.is_podcast_blocked:
 #       return HttpResponseForbidden
#    else:
        podcast = podcast.objects.get(pk=pk)
        if podcast.is_podcast_blocked:
            return HttpResponseNotAllowed            
        else:
            serializer = podcast_Serializer(podcast , many=False)

            return Response(serializer.data)


@api_view(['POST'])
def podcast_create(request):
    serializer = podcast_Serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def podcast_update(request , pk):
    podcast = podcast.objects.get(pk=pk)
    serializer = Podcast_Serializer( instance=podcast, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_podcast(request, pk):
    podcast = podcast.objects.get(pk=pk)
    podcast.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

 #-------------------------------------------------


@api_view(['GET'])
def comments_List(request):
    _comments = comment.objects.all()
    serializer = comment_serializer(_comments , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request , pk):
    _comment = comment.objects.get(pk=pk)
    serializer = comment_serializer(_comment , many=False)

    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request):
    serializer = comment_serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def comment_update(request , pk):
    _comment = comment.objects.get(pk=pk)
    serializer =comment_serializer( instance=_comment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_comment(request, pk):
    _comment = comment.objects.get(pk=pk)
    _comment.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
