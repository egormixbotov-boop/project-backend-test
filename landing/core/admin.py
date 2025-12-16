from django.contrib import admin
from .models import UsersInfo, UsersCounter


@admin.register(UsersInfo)
class UsersInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "created_at")
    search_fields = ("name", "email")
    ordering = ("-created_at",)


@admin.register(UsersCounter)
class UsersCounterAdmin(admin.ModelAdmin):
    list_display = ("id", "count")
