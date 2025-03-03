from django.db import models

# Create your models here.
class Station(models.Model):
    stationName = models.CharField(max_length=255)
    trainLine = models.CharField(max_length=255)
    leftETA = models.IntegerField(null=True)
    rightETA = models.IntegerField(null=True)
    leftCurrentDensity = models.CharField(max_length=255, null=True)
    rightCurrentDensity = models.CharField(max_length=255, null=True)
    leftHistory = models.CharField(max_length=255, null=True) # to be changed
    rightHistory = models.CharField(max_length=255, null=True) # to be changed
    leftCCTV = models.CharField(max_length=255, null=True)
    rightCCTV = models.CharField(max_length=255, null=True)
    isOperating = models.BooleanField(default=True)
    stationIMG = models.CharField(max_length=255) # img url here; to change later (models.ImageField(upload_to=''))
