from django.urls import path

from posts.views import PostCreateView, PostListView

urlpatterns = [
    path("", PostListView.as_view()),
    path("new/", PostCreateView.as_view()),
]
