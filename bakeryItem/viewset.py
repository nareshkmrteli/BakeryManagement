from rest_framework import filters, pagination, parsers, permissions, viewsets
from utility.utility import CsrfExemptSessionAuthentiation

from .models import BakeryIngredient, BakeryItem, Ingredient
from .serializer import (BakeryIngredientSerializer, BakeryItemSerializer,
                         IngredientSerializer)


class BakeryItemViewSet(viewsets.ModelViewSet):
    serializer_class=BakeryItemSerializer
    parser_classes=[parsers.JSONParser,parsers.MultiPartParser]
    permission_classes=[permissions.IsAdminUser]
    pagination_class=pagination.PageNumberPagination
    pagination_class.page_size=5
    filter_backends=[filters.SearchFilter]
    search_fields=['product__name','product__description']
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=BakeryItem.objects.all()

class BakeryIngredientViewSet(viewsets.ModelViewSet):
    serializer_class=BakeryIngredientSerializer
    parser_classes=[parsers.JSONParser,parsers.MultiPartParser]
    permission_classes=[permissions.IsAdminUser]
    pagination_class=pagination.PageNumberPagination
    pagination_class.page_size=5
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=BakeryIngredient.objects.all()

class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class=IngredientSerializer
    parser_classes=[parsers.JSONParser,parsers.MultiPartParser]
    permission_classes=[permissions.IsAdminUser]
    pagination_class=pagination.PageNumberPagination
    pagination_class.page_size=5
    filter_backends=[filters.SearchFilter]
    search_fields=['name']
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=Ingredient.objects.all()
