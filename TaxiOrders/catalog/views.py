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
               'drivers': drivers,
               'num_drivers': num_drivers,
               }
    return render(request, 'catalog/index.html', context)


def orders_view(request):
    return render(request, "catalog/orders.html", {'var': Orders.objects.all()})


def cars_view(request):
    return render(request, "catalog/cars.html", {'var_2': Cars.objects.all()})


def drivers_view(request):
    queryset_orders = Orders.objects.select_related('drivers')
    queryset_drivers = Drivers.objects.all()

    for order in queryset_orders:
        for driver in queryset_drivers:
            full_name = f"{driver.last_name} {driver.first_name} {driver.patronymic} {driver.date_of_birth}"
            if str(order.drivers) == full_name:
                driver.order_dates += f"{order.date.date()} "

    return render(request, "catalog/drivers.html", {'var_3': queryset_drivers})