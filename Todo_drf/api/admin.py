from django.contrib import admin

# Register your models here.
from Todo_drf.api.models import Task, Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user__username', 'state')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
