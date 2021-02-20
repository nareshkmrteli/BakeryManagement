from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewset import InventoryViewSet

router=DefaultRouter()
router.register(r"inventory", InventoryViewSet,basename='inventory')
urlpatterns = [
    path("",include(router.urls)),
]
