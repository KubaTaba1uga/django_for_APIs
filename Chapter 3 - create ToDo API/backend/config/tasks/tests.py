import pytest
from django.urls import reverse
from .models import TaskModel

TASK_DATA = {
    "title": "First task",
    "body": "Learn to code",
    "date": "2022-01-04T18:42:55.725119Z",
}


@pytest.fixture
@pytest.mark.django_db
def task():
    return TaskModel.objects.create(**TASK_DATA)


class TestTaskListView:
    URL = reverse("tasks_list_url")
    STATUS_CODE = 200

    @pytest.mark.django_db
    def test_list_content(self, client, task):
        response = client.get(self.URL)
        response_data = response.json().pop()
        assert response_data.get("title") == TASK_DATA["title"]

    @pytest.mark.django_db
    def test_list_status_code(self, client, task):
        response = client.get(self.URL)
        assert response.status_code == self.STATUS_CODE


class TestTaskDetailedView:
    URL = reverse("tasks_details_url", args="1")
    STATUS_CODE = 200

    @pytest.mark.django_db
    def test_task_content(self, client, task):
        response = client.get(self.URL)
        assert response.json() == TASK_DATA

    @pytest.mark.django_db
    def test_task_status_code(self, client, task):
        response = client.get(self.URL)
        assert response.status_code == self.STATUS_CODE
