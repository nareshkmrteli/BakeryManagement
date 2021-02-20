from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from inventory.models import Inventory
from rest_framework import (decorators, filters, mixins, pagination, parsers,
                            permissions, response, viewsets)
from rest_framework.decorators import action
from utility.utility import CsrfExemptSessionAuthentiation

from .models import Order, OrderItem
from .serializer import OrderItemSerializer, OrderSerializer


class OrderViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = OrderSerializer
    parser_classes = [parsers.JSONParser,parsers.MultiPartParser,parsers.FormParser]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 5
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=Order.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    @action(methods=['post'],detail=True)
    def changestatus(self,req,pk):
        newStatus = req.data.get('status','')
        if newStatus !='':
            try:
                order = Order.objects.get(pk=pk)
                if order.status==4 or order.status==5 or order.status>int(newStatus):
                    return response.Response(data={'detail':'cant change the status'},status=409)
                elif int(newStatus) in [3,4] and not req.user.is_superuser:
                    return response.Response(data={'detail':'unauthorized'},status=403)
                order.status=newStatus
                order.save(update_fields=['status'])
                return response.Response(data=OrderSerializer(order,context={'request':req}).data)
            except(ObjectDoesNotExist):
                return response.Response(data={'detail':'object not exist'},status=404)
        else:
            return response.Response(data={'detail':'invalid data'},status=400)


class OrderItemViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = OrderItemSerializer
    parser_classes = [parsers.JSONParser,parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.PageNumberPagination
    pagination_class.page_size = 5
    authentication_classes=[CsrfExemptSessionAuthentiation]
    queryset=OrderItem.objects.all()
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(order__user=self.request.user)
        return queryset
       
    def destroy(self,req,pk):
        try:
            order = OrderItem.objects.get(pk=pk)
            order.delete()
            return response.Response(data={'detail':'Order Item deleted'})
        except(ObjectDoesNotExist):
            return response.Response(data={'data':'Order Item Not exist'},status=404)
    def create(self,req):
        bakeryItem = req.POST.get('bakeryItem')
        qty = req.POST.get('qty')
        
        if bakeryItem:
            try:
                inventory=Inventory.objects.get(pk=bakeryItem)
                order,c = Order.objects.get_or_create(status=1,defaults={'user':req.user})
                data = {
                    'order':order,
                    'qty':qty,
                    'bakeryItem':inventory.bakeryitem,
                    'costPrice':inventory.costPrice,
                    'sellingPrice':inventory.sellingPrice

                }
                if (inventory.qty - float(qty))>=0:
                    orderItem = OrderItem.objects.create(**data)
                    return response.Response(data=OrderItemSerializer(orderItem,context={'request':req}).data,status=201)
                else:
                    return response.Response(data={'detail':'out of stock'},status=409)
            
            except( ObjectDoesNotExist):
                return response.Response(data={'detail':'Order item not exist'},status=409)
            except (IntegrityError):
                return response.Response(data={'detail':'integrity issue plese make sure valid data'},status=409)
        else:
            return response.Response(data={'detail':'invalid data'}, status=400)
    def update(self,req,pk):
        qty = req.data.get('qty')
        if qty:
            try:
                orderitem = OrderItem.objects.get(pk=pk)
                orderitem.qty = qty
                orderitem.save(update_fields=['qty'])
            except(ObjectDoesNotExist):
                return response.Response(data={'detail':'Order Item not exist'})
        else:
            return response.Response(data={'detail':'bed reqest'},status=400)
