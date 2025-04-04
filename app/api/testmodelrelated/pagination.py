from rest_framework.pagination import CursorPagination

class TestModelRelatedPagination(CursorPagination):
    page_size = 10
    ordering = '-id'
    page_size_query_param = 'page_size'
    max_page_size = 100
