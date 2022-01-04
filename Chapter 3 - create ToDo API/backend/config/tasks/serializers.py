from rest_framework import serializers
from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("title", "body", "date")


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("title", "pk")
