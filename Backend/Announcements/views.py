from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Announcements
from .serializers import AnnouncementSerializer


# Create your views here.
class AnnouncementPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20

class AnnouncementListView(ListAPIView):
    queryset = Announcements.objects.all().order_by('-datetimePosted')
    serializer_class = AnnouncementSerializer
    pagination_class = AnnouncementPagination

