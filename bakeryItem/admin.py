from django.contrib import admin

from .models import BakeryIngredient, BakeryItem, Ingredient

# Register your models here.
admin.site.register([BakeryIngredient,BakeryItem,Ingredient])
