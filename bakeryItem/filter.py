from rest_framework.filters import BaseFilterBackend


class CustomFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset
