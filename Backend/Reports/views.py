from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from django.db import connection, OperationalError
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

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

    def get_queryset(self):
        if check_database_status():
            return Reports.objects.all().order_by('-datetimeReported')
        return Reports.objects.none()

    def list(self, request, *args, **kwargs):
        if not check_database_status():
            return Response({"error": "Database connection error"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return super().list(request, *args, **kwargs)


def check_database_status():
    try:
        connection.cursor()
        return True
    except OperationalError:
        return False
    
class ReportSumbitView(APIView):
    def post(self, request):
        if not check_database_status():
            return Response(
                {"error": "Database is currently unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        serializer = ReportsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        if not check_database_status():
            return Response(
                {"error": "Database is currently unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        
        report = get_object_or_404(Reports, id)
        report.delete()
        return Response({"message": "Report deleted successfully."}, status=status.HTTP_204_NO_CONTENT)