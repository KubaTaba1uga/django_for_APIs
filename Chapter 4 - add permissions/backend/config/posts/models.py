from django.db import models
from django.contrib.auth import get_user_model


class PostModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=40)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
