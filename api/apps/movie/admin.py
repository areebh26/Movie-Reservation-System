from django.contrib import admin
from .models import Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "duration_minutes", "release_date", "genre" , "poster"]
    list_filter = ["genre", "release_date"]
    search_fields = ["title",  "genre"]
    ordering = ["release_date" , "created_at"] 


