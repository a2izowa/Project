from django.contrib import admin

from .models import Cars, Drivers, Orders


class CarsAdmin(admin.ModelAdmin):
    list_display = ('mark', 'number', 'date_of_production', 'colour')
    list_filter = ('mark', 'colour')
    fields = ['mark', 'number', ('date_of_production', 'colour', 'class_of_car')]
admin.site.register(Cars, CarsAdmin)


class DriversAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'date_of_birth')
    list_filter = ('last_name', 'first_name')
admin.site.register(Drivers, DriversAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('date', 'address_from', 'address_to')
    list_filter = ('date', 'address_from', 'address_to')
    fieldsets = (
        ('Дата заказа', {
            'fields': ('date', 'drivers')}),
        ('Адреса заказа', {
            'fields': ('address_from', 'address_to')}),
        ('Дополнительная информация', {
            'fields': ('number_of_passengers', 'length')
        })
    )

admin.site.register(Orders, OrdersAdmin)


