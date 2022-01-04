from rest_framework import generics
from .models import TaskModel
from .serializers import TaskSerializer, TaskListSerializer


class TaskListView(generics.ListAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailedView(generics.RetrieveAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
