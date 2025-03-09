from django.db import models
from django.utils import timezone

# Create your models here.
class Reports(models.Model):
    subject = models.CharField(max_length=255)
    station = models.CharField(max_length=50)
    body = models.TextField()
    datetimeReported = models.DateTimeField(default=timezone.now, editable=False)
