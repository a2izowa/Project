from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars', views.cars, name='cars'),
    path('drivers', views.drivers, name='drivers'),
    path('orders', views.orders, name='orders'),
]
