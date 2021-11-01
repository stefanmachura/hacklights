from django.urls import path

from profiles.views import UserListView

urlpatterns = [
    path("", UserListView.as_view()),
]
