import pytest

from posts.models import Post
from django.contrib.auth.models import User


@pytest.fixture
def user():
    user_data = {
        "username": "user1",
        "email": "user@example.com",
        "password": "password",
    }
    return User.objects.create_user(**user_data)


@pytest.fixture
def post(user):
    post_data = {"title": "title", "url": "http://google.com", "author": user}
    return Post.objects.create(**post_data)
