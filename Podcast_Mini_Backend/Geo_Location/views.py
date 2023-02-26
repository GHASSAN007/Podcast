from django.shortcuts import render
from ipware import get_client_ip
import requests

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from .serializers import location_serializer

from .models import location

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List_locations' : '/location-list/',
        'Add_location': '/location-add/',
        'delete':'/delete/',
    }

    return Response(api_urls)

@api_view(['GET'])
def location_List(request):
    geo_location = location.objects.all()
    serializer = location_serializer(geo_location, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def get_ip(request):
    ip, _ = get_client_ip(request)
    response = request.get(f'http://api.ipstack.com/{ip}?access_key=da61af9bc4bf29d265473db7385716dd')
    location_data = response.json()
    serializer = location_serializer(data=request.location_data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def delete(request):
    
    serialize = location_serializer(data=request.data)

    return Response(serialize.data)