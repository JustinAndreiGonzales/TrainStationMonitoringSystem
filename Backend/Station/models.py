from django.db import models
from django.utils import timezone


# Create your models here.
class Station(models.Model):
    stationName = models.CharField(max_length=255)
    trainLine = models.CharField(max_length=255)
    leftETA = models.DateTimeField(default=timezone.now, editable=False, null=True)
    rightETA = models.DateTimeField(default=timezone.now, editable=False, null=True)
    leftCurrentDensity = models.CharField(max_length=255, null=True)
    rightCurrentDensity = models.CharField(max_length=255, null=True)
    leftCCTV = models.CharField(max_length=255, null=True)
    rightCCTV = models.CharField(max_length=255, null=True)
    isOperating = models.BooleanField(default=True)
    stationIMG = models.CharField(max_length=255) # img url here; to change later (models.ImageField(upload_to=''))
    stationImage = models.TextField(max_length=255)


class HourlyDensity(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    leftDensity = models.FloatField(null=True)
    rightDensity = models.FloatField(null=True)


class DailyDensity(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now, editable=False)
    leftDensity = models.FloatField(null=True)
    rightDensity = models.FloatField(null=True)
