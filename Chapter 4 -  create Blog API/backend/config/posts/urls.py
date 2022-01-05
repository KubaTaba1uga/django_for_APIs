from django.urls import path
from .views import (
    PostListView,
    PostDetailsView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
)

urlpatterns = [
    path("list", PostListView.as_view(), name="post_list_url"),
    path("create", PostCreateView.as_view(), name="post_create_url"),
    path("<int:pk>", PostDetailsView.as_view(), name="post_details_url"),
    path("<int:pk>/update", PostUpdateView.as_view(), name="post_update_url"),
    path("<int:pk>/delete", PostDeleteView.as_view(), name="post_delete_url"),
]
