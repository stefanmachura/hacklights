import pytest

from django.contrib.auth.models import User


@pytest.fixture
def user():
    user_data = {
        "username": "user1",
        "email": "user@example.com",
        "password": "password",
    }
    return User.objects.create_user(**user_data)
