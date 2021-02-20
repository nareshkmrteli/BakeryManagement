from rest_framework import filters, pagination, parsers, permissions, viewsets
from utility.utility import CsrfExemptSessionAuthentiation

from .models import Inventory
from .serializer import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    parser_classes = [parsers.JSONParser,parsers.MultiPartParser]
    permission_classes = [permissions.IsAdminUser]
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 5
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['bakeryitem__name','bakeryitem__description']
    ordering_fields=['costPrice','sellingPrice']
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=Inventory.objects.all()
