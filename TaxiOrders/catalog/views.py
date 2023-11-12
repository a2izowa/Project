from django.shortcuts import render
from .models import Cars, Drivers, Orders
from django.views.generic import ListView

def index(request):
    cars = Cars.objects.all()
    num_cars = Cars.objects.all().count()
    orders = Orders.objects.all()
    num_orders = Orders.objects.all().count()
    drivers = Drivers.objects.all()
    num_drivers = Drivers.objects.all().count()
    context = {'cars': cars,
               'num_cars': num_cars,
               'orders': orders,
               'num_orders': num_orders,
               'drivers':  drivers,
               'num_drivers': num_drivers,
               }
    return render(request, 'catalog/index.html', context)


def orders(request):
    orders = Orders.objects.all()
    return render(request, "catalog/orders.html", {
        'var' : orders,
    })

def cars(request):
    cars = Cars.objects.all()
    return render(request, "catalog/cars.html", {
        'var_2' : cars,
    })


def drivers(request):
    drivers = Drivers.objects.all()
    return render(request, "catalog/drivers.html", {
        'var_3' : drivers,
    })
