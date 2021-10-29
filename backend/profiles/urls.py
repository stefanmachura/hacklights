from django.urls import path

from profiles.views import UserListView, ProfileListView

urlpatterns = [
    path("", UserListView.as_view()),
    path("prof/", ProfileListView.as_view()),
]
