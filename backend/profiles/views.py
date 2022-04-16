from django.contrib.auth.models import User
from profiles.serializers import UserSerializer
from rest_framework import generics


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
