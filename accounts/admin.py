from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'is_staff', 'slug', 'is_active')


admin.site.register(User)