from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdminUser

# Register your models here.
class AdminAdmin(UserAdmin):
    model = AdminUser

admin.site.register(AdminUser, AdminAdmin)
