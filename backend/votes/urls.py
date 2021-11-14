from django.urls import path

from votes.views import PostVoteView, PostUnvoteView

urlpatterns = [
    path("vote/<int:pk>", PostVoteView.as_view()),
    path("unvote/<int:pk>", PostUnvoteView.as_view()),
]
