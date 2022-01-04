from django.shortcuts import render
from django.views import generic
from .models import BookModel


class BookListView(generic.ListView):
    model = BookModel
    template_name = "list_books.html"
