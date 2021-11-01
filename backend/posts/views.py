from posts.models import Post
from posts.paginations import PostListPagination
from posts.serializers import PostListSerializer, PostCreateSerializer
from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-pub_date")
    serializer_class = PostListSerializer
    pagination_class = PostListPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["pub_date", "score"]


class PostCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer
