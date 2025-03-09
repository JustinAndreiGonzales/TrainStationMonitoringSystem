from django.db import models
from django.utils import timezone

# Create your models here.
class Announcements(models.Model):
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    datetimePosted = models.DateTimeField(default=timezone.now, editable=False)
