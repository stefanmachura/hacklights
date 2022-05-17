from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post
from votes.serializers import PostUpdateSerializer
from votes.permissions import IsNotOwner


class PostVoteView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsNotOwner]
    queryset = Post.objects.all()

    def patch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.score += 1
        post.save()
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUnvoteView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsNotOwner]
    queryset = Post.objects.all()

    def patch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.score -= 1
        post.save()
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
