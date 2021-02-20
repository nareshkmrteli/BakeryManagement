from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewset import (BakeryIngredientViewSet, BakeryItemViewSet,
                      IngredientViewSet)

router=DefaultRouter()
router.register(r"bakeryingredient", BakeryIngredientViewSet,basename='bakeryingredient')
router.register(r"bakeryitem", BakeryItemViewSet,basename='bakeryitem')
router.register(r'ingredient',IngredientViewSet,basename='ingredient')
urlpatterns = [
    path("",include(router.urls)),
]
