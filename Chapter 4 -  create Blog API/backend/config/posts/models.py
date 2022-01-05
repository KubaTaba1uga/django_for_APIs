from django.db import models


class PostModel(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    creation_date = models.DateTime(auto_now_add=True)
    modification_date = models.DateTime(auto_add=True)
