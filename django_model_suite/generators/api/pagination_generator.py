from django_model_suite.generators.base import BaseGenerator


class PaginationGenerator(BaseGenerator):
    def generate(self, fields: list) -> None:
        content = f"""from rest_framework.pagination import CursorPagination

class {self.model.__name__}Pagination(CursorPagination):
    page_size = 10
    ordering = '-id'
    page_size_query_param = 'page_size'
    max_page_size = 100
"""
        self.write_file("pagination.py", content)
