from django.db import models

# Create your models here.

class Station(models.Model):
    stationName = models.CharField(max_length=255)
    trainLine = models.CharField(max_length=255)
    leftETA = models.IntegerField()
    rightETA = models.IntegerField()
    leftCurrentDensity = models.CharField(max_length=255)
    rightCurrentDensity = models.CharField(max_length=255)
    leftHistory = models.CharField(max_length=255) # to be changed
    rightHistory = models.CharField(max_length=255) # to be changed
    cctv = models.CharField(max_length=255)
    isOperating = models.BooleanField(default=True)
    stationIMG = models.CharField(max_length=255) # img url here; to change later (models.ImageField(upload_to=''))

class Train(models.Model):
    trainLine = models.CharField(max_length=255)
    ocation = models.CharField(max_length=255)
    currentStatus = models.CharField(max_length=255)