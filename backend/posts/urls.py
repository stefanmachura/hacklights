from django.urls import path

from posts.views import PostListView, PostCreateView

urlpatterns = [
    path("", PostListView.as_view()),
    path("new/", PostCreateView.as_view()),
]
