from rest_framework import serializers
from posts.models import Post
from rest_framework.serializers import ValidationError


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "url", "author"]
        extra_kwargs = {"author": {"required": True, "allow_null": False}}
