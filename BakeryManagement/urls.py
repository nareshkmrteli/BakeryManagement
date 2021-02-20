from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bakeryitem/',include('bakeryItem.urls')),
    path('inventory/',include('inventory.urls')),
    path('user/',include('user.urls')),
    path('order/',include('order.urls')),
    path(r"restapi/",include("rest_framework.urls")),  
    
]
