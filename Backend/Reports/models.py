from django.db import models

# Create your models here.
class Reports(models.Model):
    subject = models.CharField(max_length=255)
    station = models.CharField(max_length=50)
    body = models.TextField()
    datetimeReported = models.DateTimeField(auto_now_add=True)
