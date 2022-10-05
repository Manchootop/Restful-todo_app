from django.contrib import admin

# Register your models here.
from Todo_drf.api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
