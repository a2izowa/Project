from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from catalog import views

urlpatterns = [
    path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('cars', views.cars),
    path('drivers', views.drivers),
    path('orders', views.orders),
]
