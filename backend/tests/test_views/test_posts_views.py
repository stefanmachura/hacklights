from datetime import datetime

import pytest

from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_empty_post_list():
    client = APIClient()
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
    }


@pytest.mark.django_db
def test_single_post_list(post):
    client = APIClient()
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "author": post.author.username,
                "pub_date": datetime.strftime(post.pub_date, "%Y-%m-%dT%H:%M:%S.%fZ"),
                "score": post.score,
                "title": post.title,
                "url": post.url,
            }
        ],
    }
