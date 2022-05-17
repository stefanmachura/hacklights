import pytest
from freezegun import freeze_time

from posts.models import Post
from posts.serializers import PostCreateSerializer, PostListSerializer


@pytest.mark.django_db
def test_post_list_serializer(user):
    post_data = {"title": "title", "url": "http://google.com", "author": user}

    expected_serializer_data = {
        "title": "title",
        "url": "http://google.com",
        "author": "user1",
    }
    serializer = PostListSerializer(post_data)
    print(serializer.data)
    assert serializer.data == expected_serializer_data


@freeze_time("2021-12-01")
@pytest.mark.django_db
def test_created_post_list_serializer(user):
    post_data = {"title": "title", "url": "http://google.com", "author": user}

    expected_serializer_data = {
        "title": "title",
        "url": "http://google.com",
        "author": "user1",
        "score": 0,
        "pub_date": "2021-12-01T00:00:00Z",
    }

    post = Post.objects.create(**post_data)

    serializer = PostListSerializer(post)
    print(serializer.data)
    assert serializer.data == expected_serializer_data


@pytest.mark.django_db
def test_post_create_serializer(user):
    data = {"title": "title", "url": "http://google.com", "author": user}
    expected_serializer_data = {
        "title": "title",
        "url": "http://google.com",
        "author": user.pk,
    }

    serializer = PostCreateSerializer(data)
    assert serializer.data == expected_serializer_data
