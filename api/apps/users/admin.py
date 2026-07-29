from django.contrib import admin
from apps.users.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email","name","phone","gender","profile_pic","is_active","is_staff","is_superuser"]
    list_filter = ["gender","is_staff","is_superuser"]
    search_fields = ["email","name","phone"]
    ordering = ["date_joined"]
