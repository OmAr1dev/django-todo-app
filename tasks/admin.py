from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin configuration for Task model.

    Displays task title, completion status, and timestamps.
    Allows filtering by completion status and creation date,
    and searching by title or description.
    """

    list_display = ("title", "completed", "created_at", "updated_at")
    list_filter = ("completed", "created_at")
    search_fields = ("title", "description")
