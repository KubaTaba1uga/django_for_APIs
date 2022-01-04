"""
        Serializer translate data into a format that is 
                easy to consume over the interner.
                Usually JSON or XML.
"""

from rest_framework import serializers
from books.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    """ModelSerializer uses meta class protocol"""

    class Meta:
        # Model which will be serialized
        model = BookModel
        # Fields which will be exposed
        fields = ("title", "subtitle", "author", "isbn")
