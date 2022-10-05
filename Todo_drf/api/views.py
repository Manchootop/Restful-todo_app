from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<int:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<int:pk>/',
        'Delete': '/task-delete/<int:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
