from rest_framework.filters import BaseFilterBackend


class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if 'search' in request.query_params:
            queryset=queryset.filter(name__contains =request.query_params['search'])
        if 'product' in request.query_params:
            queryset=queryset.filter(product =request.query_params['product'])
        return queryset
