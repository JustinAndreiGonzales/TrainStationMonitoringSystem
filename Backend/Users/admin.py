from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin

# Register your models here.
class AdminAdmin(UserAdmin):
    model = Admin

admin.site.register(Admin, AdminAdmin)
