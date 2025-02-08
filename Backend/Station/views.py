from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db import DatabaseError

from .models import Station
from .serializers import StationSerializer

# Create your views here.
@api_view(['GET'])
def get_all_station(request):
    try:
        stations = Station.objects.values('id', 'stationName', 'trainLine', 'isOperating')
        return Response(stations)
    except DatabaseError:
        return Response(
            {"error": "Database error occured while fetching stations."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        return Response(
            {"error": f"An unexpected error occured: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_station(request, id):
    station = get_object_or_404(Station, id = id)
    serializer = StationSerializer(station)
    return Response(serializer.data)