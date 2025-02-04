from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField()
    eta = models.IntegerField()