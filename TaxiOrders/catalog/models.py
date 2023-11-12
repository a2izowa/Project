from django.db import models
from django.urls import reverse

# автомобили
class Cars(models.Model):
    mark = models.CharField(max_length=20,
                            help_text="Введите марку машины",
                            verbose_name="Марка")
    class_of_car = models.CharField(max_length=6,
                                    help_text="Введите класс машины (эконом/бизнес)",
                                    verbose_name="Эконом/Бизнес")
    number = models.CharField(db_index=True, max_length=9,
                              help_text="Введите номер машины",
                              verbose_name="Номер")
    colour = models.CharField(max_length=15,
                              help_text="Введите цвет машины",
                              verbose_name="Цвет")
    date_of_production = models.TextField(max_length=4,
                                          help_text="Введите год выпуска машины",
                                          verbose_name="Дата производства")

    class Meta:
        ordering = ["mark"]

    def __str__(self):
        return '%s %s %s' % (self.mark, self.date_of_production, self.number)

    def get_absolute_url(self):
        return reverse('cars-detail', args=[str(self.id)])


class Drivers(models.Model):
    last_name = models.CharField(max_length=20,
                                 help_text="Введите фамилию",
                                 verbose_name="Фамилия")
    first_name = models.CharField(max_length=20,
                                  help_text="Введите имя",
                                  verbose_name="Имя")
    patronymic = models.CharField(max_length=20,
                                  help_text="Введите отчество",
                                  verbose_name="Отчество")
    date_of_birth = models.DateField(help_text="Введите год рождения",
                                     verbose_name="Дата рождения")
    INN = models.DecimalField(db_index=True, decimal_places=0, max_digits=12,
                              help_text="Введите ИНН",
                              verbose_name="ИНН")
    passport = models.CharField(max_length=11,
                           help_text="Введите номер и серию паспорта",
                           verbose_name="Паспорт")
    cars = models.ForeignKey('Cars',
                             on_delete=models.CASCADE,
                             verbose_name="Автомобили", null=True)
    class Meta:
        ordering = ["last_name"]

    def __str__(self):
        return '%s %s %s %s' % (self.last_name, self.first_name, self.patronymic, self.date_of_birth)

    def get_absolute_url(self):
        return reverse('drivers-detail', args=[str(self.id)])
    def display_cars(self):
        return ', '.join([cars.mark for cars in
                         self.cars.all()])
    display_cars.short_description = 'Машины'


class Orders(models.Model):
    date = models.DateTimeField(db_index=True, help_text="Введите дату и время заказа",
                                verbose_name="Дата и время",
                                )
    address_from = models.TextField(help_text="Введите адрес подачи такси",
                                    verbose_name="Адрес подачи")
    address_to = models.TextField(help_text="Введите адрес следования",
                                  verbose_name="Адрес следования")
    number_of_passengers = models.DecimalField(decimal_places=0, max_digits=1,
                                               help_text="Введите количество пассажиров",
                                               verbose_name="Количество пассажиров")
    length = models.DecimalField(decimal_places=2, max_digits=6,
                                 help_text="Введите длину маршрута в километрах",
                                 verbose_name="Длина маршрута")
    drivers = models.ForeignKey('Drivers', null=True,
                             on_delete=models.CASCADE,
                             verbose_name="Водитель")

    class Meta:
        ordering = ["date"]
    def __str__(self):
        return '%s %s %s' % (self.date, self.address_from, self.address_to)

    def get_absolute_url(self):
        return reverse('orders-detail', args=[str(self.id)])

    def display_drivers(self):
        return ', '.join([drivers.last_name for drivers in
                          self.drivers.all()])

    display_drivers.short_description = 'Водители'