from rest_framework import status
from rest_framework.response import Response
from .serializers import location_serializer
from rest_framework.views import APIView
from .models import location

class api_over_view(APIView):
    def apiOverview(request):
        api_urls={
            'List_locations' : '/location-list/',
            'Add_location': '/location-add/',
            'delete':'/delete/',
        }

        return Response(api_urls)

class location_list(APIView):
    def location_List(request):
        geo_location = location.objects.all()
        serializer = location_serializer(geo_location, many=True)
        return Response(serializer.data)


class user_location(APIView):
    def post(self,request):
        serialize = location_serializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
