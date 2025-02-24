from rest_framework.generics import ListAPIView
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

    def list(self, request, *args, **kwargs):
        if check_database_status():
            queryset = Announcements.objects.all().order_by('-datetimePosted')

            if queryset is None:
                return Response({"error": "Database connection error"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            return Response(
                {"error": "Database connection error"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        return super().list(request, *args, **kwargs)


def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False