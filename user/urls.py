from django.urls import path

from .views import create, login, logout

urlpatterns = [
    path('create/',create,name='create'),
    path('login/',login,name='login'),
    path('logout/',logout, name='logout'),
]
