import pytest

from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_post_list():
    client = APIClient()
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
    }
