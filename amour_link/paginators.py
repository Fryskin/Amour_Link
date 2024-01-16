from rest_framework.pagination import PageNumberPagination


class FormPaginator(PageNumberPagination):
    page_size = 1
