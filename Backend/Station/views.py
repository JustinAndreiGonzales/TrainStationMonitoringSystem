from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import OperationalError, connection

from .models import Station, HourlyDensity, DailyDensity
from .serializers import StationSerializer

# Create your views here.
@api_view(['GET'])
def get_all_station(request):
    if check_database_status():
        stations = Station.objects.values('id', 'stationName', 'trainLine', 'isOperating')
        return Response(stations)
    else:
        return Response(
            {"error": "Database is currently unavailable. Please try again later."},
            status=status.HTTP_503_SERVICE_UNAVAILABLE
        )


@api_view(['GET'])
def get_station(request, id):
    station = get_object_or_404(Station, id=id)
    serializer = StationSerializer(station)
    return Response(serializer.data)


@api_view(['GET'])
def get_current_density(request, id, platform_side):
    station = get_object_or_404(Station, id=id)

    # Check availability of CCTVs
    if not station.leftCCTV and not station.rightCCTV:
        return Response({"error": "Cannot fetch data. No CCTVs available for this station."}, status=404)

    match platform_side:
        case "left":
            if not station.leftCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)

            return Response({"leftCurrentDensity": station.leftCurrentDensity})            
        case "right":
            if not station.rightCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)

            return Response({"rightCurrentDensity": station.rightCurrentDensity})
        case _:
            return Response({"error": "Invalid URI"}, status=404)


def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False
    

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "You are connected!"})
    
    # in Header
    # Authentication: Bearer <access key>


@api_view(['GET'])
def get_cctv_feed(request, id, platform_side):
    station = get_object_or_404(Station, id=id)

    # Check availability of CCTVs
    if not station.leftCCTV and not station.rightCCTV:
        return Response({"error": "No CCTVs available for this station."}, status=404)

    match platform_side:
        case "left":
            if not station.leftCCTV:
                return Response({"error": "Selected CCTV is unavailable for this station."}, status=404)
            return Response({"leftCCTV": station.leftCCTV})
        case "right":
            if not station.rightCCTV:
                return Response({"error": "Selected CCTV is unavailable for this station."}, status=404)
            return Response({"rightCCTV": station.rightCCTV})
        case _:
            return Response({"error": "Invalid URI"}, status=404)


@api_view(['GET'])
def get_hourly_density(request, id, platform_side):
    station = get_object_or_404(Station, id=id)

    # Check availability of CCTVs
    if not station.leftCCTV and not station.rightCCTV:
        return Response({"error": "Cannot fetch data. No CCTVs available for this station."}, status=404)

    match platform_side:
        case "left":
            if not station.leftCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)

            hourly_densities = HourlyDensity.objects.filter(station_id=id).values("id", "station_id", "leftDensity")
    
            if not hourly_densities.exists():
                return Response({"error": "No hourly density records found for the given station id"}, status=404)

            return Response(hourly_densities, status=200)
        case "right":
            if not station.rightCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)
                
            hourly_densities = HourlyDensity.objects.filter(station_id=id).values("id", "station_id", "rightDensity")
    
            if not hourly_densities.exists():
                return Response({"error": "No hourly density records found for the given station id"}, status=404)

            return Response(hourly_densities, status=200)
        case _:
            return Response({"error": "Invalid URI"}, status=404)


@api_view(['GET'])
def get_daily_density(request, id, platform_side):
    station = get_object_or_404(Station, id=id)

    # Check availability of CCTVs
    if not station.leftCCTV and not station.rightCCTV:
        return Response({"error": "Cannot fetch data. No CCTVs available for this station."}, status=404)

    match platform_side:
        case "left":
            if not station.leftCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)

            daily_densities = DailyDensity.objects.filter(station_id=id).values("id", "station_id", "leftDensity")
    
            if not daily_densities.exists():
                return Response({"error": "No daily density records found for the given station id"}, status=404)

            return Response(daily_densities, status=200)
        case "right":
            if not station.rightCCTV:
                return Response({"error": "Cannot fetch data. CCTV is unavailable."}, status=404)
                
            daily_densities = DailyDensity.objects.filter(station_id=id).values("id", "station_id", "rightDensity")
    
            if not daily_densities.exists():
                return Response({"error": "No daily density records found for the given station id"}, status=404)

            return Response(daily_densities, status=200)
        case _:
            return Response({"error": "Invalid URI"}, status=404)
