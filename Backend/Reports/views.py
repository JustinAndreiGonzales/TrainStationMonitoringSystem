from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .models import Reports
from .serializers import ReportsSerializer

# Create your views here.
class ReportsPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class ReportsListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reports.objects.all().order_by('-datetimeReported')
    serializer_class = ReportsSerializer
    pagination_class = ReportsPagination