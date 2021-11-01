from rest_framework import pagination


class PostListPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = "p"
