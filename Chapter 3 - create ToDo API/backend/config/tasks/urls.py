from django.urls import path
from .views import TaskListView, TaskDetailedView

urlpatterns = [
    path("list", TaskListView.as_view(), name="tasks_list_url"),
    path("<int:pk>", TaskDetailedView.as_view(), name="tasks_details_url"),
]
