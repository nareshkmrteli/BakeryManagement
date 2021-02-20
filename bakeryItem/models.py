from django.db import models


class BakeryItem(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name

class BakeryIngredient(models.Model):
    product = models.ForeignKey(BakeryItem,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.PROTECT)
    qtyPercentage = models.FloatField(null=False)
    def __str__(self):
        return self.id




    