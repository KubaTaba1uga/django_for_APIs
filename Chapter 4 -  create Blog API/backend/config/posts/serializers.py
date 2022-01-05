from rest_framework import serializers
from .models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("title", "body", "creation_date", "modification_date")


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("title", "creation_date")
