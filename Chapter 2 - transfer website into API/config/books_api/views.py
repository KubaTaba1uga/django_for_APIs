from rest_framework import generics
from books.models import BookModel
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """ListAPIView need at least two fields"""

    # Queryset specify which objects will be exposed
    queryset = BookModel.objects.all()
    # Serializer_class specify how queryset data
    #   will be handled
    serializer_class = BookSerializer
