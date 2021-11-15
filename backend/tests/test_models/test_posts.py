import pytest

from posts.models import Post


@pytest.mark.django_db
def test_post_creation(user):
    post_data = {"title": "title", "url": "http://google.com", "author": user}
    post = Post.objects.create(**post_data)
    assert post.title == "title"
    assert post.url == "http://google.com"
    assert post.author == user
    assert post.score == 0


@pytest.mark.django_db
def test_deleting_user_nulls_author_of_their_posts(user):
    post_data = {"title": "title", "url": "http://google.com", "author": user}
    post = Post.objects.create(**post_data)
    assert post.author == user
    user.delete()
    post = Post.objects.get(pk=post.pk)
    assert post.author is None
