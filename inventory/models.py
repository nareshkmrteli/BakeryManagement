from bakeryItem.models import BakeryItem
from django.db import models


# Create your models here.
class Inventory(models.Model):
    bakeryitem = models.ForeignKey(BakeryItem,on_delete=models.CASCADE)
    costPrice = models.FloatField(null=False)
    sellingPrice = models.FloatField(null=False)
    qty = models.FloatField(null=False)
