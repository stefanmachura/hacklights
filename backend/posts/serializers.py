from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ["title", "url", "author", "score", "pub_date"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "url", "author"]
        extra_kwargs = {"author": {"required": True, "allow_null": False}}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
