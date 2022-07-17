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
        'List_stories':'/stories-list/',               
        'story_Detailview':'/story-view/<str:pk>',
        'Create_story':'/create-story/',
        'Update_story': '/story-update/<str:pk>/',
        'Delete_story': '/story-delete/<str:pk>/',

    }

    return Response(api_urls)

@api_view(['GET'])
def List_stories(request):
    stores = story.objects.all()
    serializer = story_serializer(stores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def story_detail(request , pk):
    story = story.objects.get(pk=pk)
    serializer = story_serializer(story, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def Create_story(request):
    serializer = story_serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def Update_story(request , pk):
    story = story.objects.get(pk=pk)
    serializer = story_serializer( instance=story, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete_story(request, pk):
    story = story.objects.get(pk=pk)
    story.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

