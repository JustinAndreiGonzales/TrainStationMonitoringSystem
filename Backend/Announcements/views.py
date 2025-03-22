from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.db import OperationalError, connection
from rest_framework.response import Response
from rest_framework import status

from .models import Announcements
from .serializers import AnnouncementSerializer


# Create your views here.
class AnnouncementPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class AnnouncementListView(ListAPIView):
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination

    def get_queryset(self):
        if check_database_status():
            return Announcements.objects.all().order_by('-datetimePosted')
        return Announcements.objects.none()

    def list(self, request, *args, **kwargs):
        if not check_database_status():
            return Response({"error": "Database connection error"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return super().list(request, *args, **kwargs)
    
class AnnouncementCreateView(APIView):
    def post(self, request):
        if not check_database_status():
            return Response(
                {"error": "Database is currently unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnnouncementUpdateView(APIView):
    def put(self, request, pk):
        if not check_database_status():
            return Response(
                {"error": "Database is currently unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        try:
            announcement = Announcements.objects.get(pk=pk)
        except:
            return Response(
                {"error": "Announcement not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = AnnouncementSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False
