from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from inventory.models import BakeryItem


# Create your models here.
class Order(models.Model):
    class Meta:
        ordering=['-id']
    class choices(models.IntegerChoices):
        CART = 1
        PLACED = 2
        DISPATCHED = 3
        DELIVERED = 4
        CANCEL = 5
    user = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True)
    status = models.SmallIntegerField(choices=choices.choices,default=choices.CART)
    discount = models.FloatField(default=0)

class OrderItem(models.Model):
    ordering = ['-id']
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    qty = models.FloatField(null=False,validators=[MinValueValidator(1,message='minimum 1 qty is mst include')])
    bakeryItem = models.ForeignKey(BakeryItem,on_delete=models.SET_NULL,null=True)
    costPrice = models.FloatField(null=False)
    sellingPrice = models.FloatField(null=False)

    
