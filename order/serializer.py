from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    class Meta:
        model = Order
        fields = ['url','id','user','status','discount']
        read_only_fields=['status','discount']
    
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['url','id','order','qty','bakeryItem','costPrice','sellingPrice']
        read_only_fields=['order','costPrice','sellingPrice']
    
