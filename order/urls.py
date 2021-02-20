from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewset import OrderItemViewSet, OrderViewSet

router=DefaultRouter()
router.register(r"order", OrderViewSet,basename='order')
router.register(r"orderitem", OrderItemViewSet,basename='orderitem')

urlpatterns = [
    path("",include(router.urls)),
]
