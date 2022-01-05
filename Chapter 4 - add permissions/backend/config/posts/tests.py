import pytest
from django.urls import reverse
from .models import PostModel


POST_DATA = {"title": "Hello Friend", "body": "This is my first post"}


@pytest.fixture
@pytest.mark.django_db
def post():
    return PostModel.objects.create(**POST_DATA)


class TestPostListView:
    URL = reverse("post_list_url")
    STATUS_CODE = 200

    @pytest.mark.django_db
    def test_list_content(self, client, post):
        response = client.get(self.URL)
        post_instance = response.json().pop()
        assert post_instance["title"] == POST_DATA["title"]
        assert post_instance["body"] == POST_DATA["body"]

    @pytest.mark.django_db
    def test_list_status_code(self, client, post):
        response = client.get(self.URL)
        assert response.status_code == self.STATUS_CODE


class TestPostDetailsView:
    URL = "post_details_url"
    STATUS_CODE = 200

    def reverse_url(self, post_pk):
        return reverse(self.URL, args=(post_pk,))

    @pytest.mark.django_db
    def test_details_content(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.get(url)
        post_instance = response.json()
        assert post_instance["title"] == POST_DATA["title"]
        assert post_instance["body"] == POST_DATA["body"]

    @pytest.mark.django_db
    def test_details_status_code(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.get(url)
        assert response.status_code == self.STATUS_CODE


class TestPostCreateView:
    URL = reverse("post_create_url")
    STATUS_CODE = 201

    @pytest.mark.django_db
    def test_post_creation(self, client):
        response = client.post(self.URL, data=POST_DATA)
        post_instance = response.json()
        assert post_instance["title"] == POST_DATA["title"]
        assert post_instance["body"] == POST_DATA["body"]

    @pytest.mark.django_db
    def test_creation_status_code(self, client, post):
        response = client.post(self.URL, data=POST_DATA)
        assert response.status_code == self.STATUS_CODE


class TestPostUpdateView:
    URL = "post_update_url"
    POST_DATA = {"title": "Post title modified"}
    POST_TYPE = "application/json"
    STATUS_CODE = 200

    def reverse_url(self, post_pk):
        return reverse(self.URL, args=(post_pk,))

    @pytest.mark.django_db
    def test_post_update(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.patch(url, data=self.POST_DATA, content_type=self.POST_TYPE)
        post_instance = response.json()
        assert post_instance["title"] == self.POST_DATA["title"]

    @pytest.mark.django_db
    def test_update_status_code(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.patch(url, data=self.POST_DATA, content_type=self.POST_TYPE)
        assert response.status_code == self.STATUS_CODE


class TestPostDeleteView:
    URL = "post_delete_url"
    STATUS_CODE = 204

    def reverse_url(self, post_pk):
        return reverse(self.URL, args=(post_pk,))

    @pytest.mark.django_db
    def test_post_delete(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.delete(url)
        deleted_post = PostModel.objects.filter(pk=post.pk).first()
        assert deleted_post is None

    @pytest.mark.django_db
    def test_deletion_status_code(self, client, post):
        url = self.reverse_url(post.pk)
        response = client.delete(url)
        assert response.status_code == self.STATUS_CODE
