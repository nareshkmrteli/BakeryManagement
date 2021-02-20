from rest_framework import serializers

from .models import BakeryIngredient, BakeryItem, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['url',"id","name","description"]

class BakeryIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model=BakeryIngredient
        fields=['url',"id","product","ingredient",'qtyPercentage']

class BakeryItemSerializer(serializers.ModelSerializer):
    bakeryIngredient=BakeryIngredientSerializer(many=True,required=False,read_only=True)
    class Meta:
        model=BakeryItem
        fields=["url","id","name",'description','bakeryIngredient']

