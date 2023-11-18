from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('cars', views.cars_view),
    path('drivers', views.drivers_view),
    path('orders', views.orders_view),
]