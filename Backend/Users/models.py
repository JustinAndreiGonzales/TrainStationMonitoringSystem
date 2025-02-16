from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Admin(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('superAdmin', 'Super_Admin')
    ]

    role = models.CharField(max_length=20, choices=ROLES, default='admin')

    
