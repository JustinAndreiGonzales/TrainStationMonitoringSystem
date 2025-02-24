from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from django.db import connection, OperationalError
from rest_framework.response import Response
from rest_framework import status

from .models import Reports
from .serializers import ReportsSerializer

# Create your views here.
class ReportsPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class ReportsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReportsSerializer
    pagination_class = ReportsPagination

    def list(self, request, *args, **kwargs):
        if check_database_status():
            queryset = Reports.objects.all().order_by('-datetimeReported')

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