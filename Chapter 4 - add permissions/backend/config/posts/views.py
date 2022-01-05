from rest_framework import generics
from .models import PostModel
from .serializers import PostSerializer, PostListSerializer

""" Adding permissions on views level
        which will give read capability on resources,
        however other capabilities will be available
        for logged-in users only.
"""
from rest_framework import permissions  # New


class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer


class PostDetailsView(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    # Only logged in user has this capability
    permission_classes = (permissions.IsAuthenticated,)  # New
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    # Only logged in user has this capability
    permission_classes = (permissions.IsAuthenticated,)  # New
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    # Only logged in user has this capability
    permission_classes = (permissions.IsAuthenticated,)  # New
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
