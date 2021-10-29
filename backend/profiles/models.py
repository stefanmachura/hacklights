from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=512, blank=True)
    location = models.CharField(max_length=32, blank=True)
    score = models.IntegerField(default=0)
    birthday = models.DateField(null=True)

