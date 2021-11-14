from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=512)
    score = models.IntegerField(default=0)
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.SET_NULL, null=True
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title=}, {self.author=}"
