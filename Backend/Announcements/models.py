from django.db import models

# Create your models here.
class Announcements(models.Model):
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    datetimePosted = models.DateTimeField(auto_now_add=True)
