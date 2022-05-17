import pytest
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from profiles.models import Profile


@pytest.mark.django_db
def test_user_creation_with_no_profile():
    user_data = {
        "username": "user1",
        "email": "user@example.com",
        "password": "password",
    }
    user = User.objects.create_user(**user_data)
    assert user.password != "password"
    assert user.username == "user1"
    assert user.email == "user@example.com"


@pytest.mark.django_db
def test_user_creation_with_empty_profile():
    profile = Profile()
    user_data = {
        "username": "user1",
        "email": "user@example.com",
        "password": "password",
        "profile": profile,
    }
    user = User.objects.create_user(**user_data)
    assert user.password != "password"
    assert user.username == "user1"
    assert user.email == "user@example.com"
    assert user.profile == profile


@pytest.mark.django_db
def test_user_creation_with_full_profile():
    profile_data = {
        "bio": "this is my bio",
        "location": "warsaw",
        "birthday": "2020-10-10",
    }

    profile = Profile(**profile_data)
    user_data = {
        "username": "user1",
        "email": "user@example.com",
        "password": "password",
        "profile": profile,
    }
    user = User.objects.create_user(**user_data)
    assert user.password != "password"
    assert user.username == "user1"
    assert user.email == "user@example.com"
    assert user.profile.bio == "this is my bio"
    assert user.profile.location == "warsaw"
    assert user.profile.birthday == "2020-10-10"
    assert user.profile.score == 0


@pytest.mark.django_db
def test_duplicated_username_fails():
    user_data = {
        "username": "username",
        "email": "user@example.com",
        "password": "password",
    }
    user_data2 = {
        "username": "username",
        "email": "user2@example.com",
        "password": "password",
    }
    _ = User.objects.create_user(**user_data)
    with pytest.raises(IntegrityError):
        _ = User.objects.create_user(**user_data2)
