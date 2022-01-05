from rest_framework import generics
from .models import PostModel
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDetailsView(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostUpdateView(generics.UpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(generics.DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
