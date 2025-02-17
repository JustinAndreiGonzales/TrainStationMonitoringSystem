from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AdminUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SUPER_ADMIN = 'superAdmin', 'Super Admin'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)
    name = models.CharField(max_length=100, null=True, blank=True)

    
