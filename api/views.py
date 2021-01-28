from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


# Create your views here.

@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        'List': '/task-list/',
        'Detail': '/task-detail',
        'Create': '/task-create/',
        'Update': '/task-update/',
        'Delete': '/task-delete/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST', 'PUT'])
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response("Item was successfully deleted!")
