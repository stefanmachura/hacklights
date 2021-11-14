from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from votes.serializers import PostUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Post


class PostVoteView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()

    def patch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.author is None or post.author.pk == request.user.pk:
            return Response(
                {
                    "error": "You cannot vote on a post that has no author, or you are its author"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        post.score += 1
        post.save()
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUnvoteView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()

    def patch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if post.author is None or post.author.pk == request.user.pk:
            return Response(
                {
                    "error": "You cannot vote on a post that has no author, or you are its author"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        post.score -= 1
        post.save()
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
