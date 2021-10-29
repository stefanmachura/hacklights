from django.contrib.auth.models import User
from profiles.models import Profile
from profiles.serializers import ProfileSerializer, UserSerializer
from rest_framework import generics


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
