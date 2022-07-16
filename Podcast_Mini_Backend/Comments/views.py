from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from django.http import HttpResponseNotAllowed , Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  commentSerializer

from .models import *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
                'List_comments':'/comments-list/',
        'comment_Detailview':'comment-view/<str:pk>',
        'Create_comment':'/create-comment/',
        'Update-comment': '/comment-update/<str:pk>/',
        'Delete_comment': '/comment-delete/<str:pk>/',
    }
    return Response(api_urls)


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

 