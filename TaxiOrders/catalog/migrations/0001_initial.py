# Generated by Django 4.2.7 on 2023-11-11 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(help_text='Введите марку машины', max_length=20, verbose_name='Марка')),
                ('class_of_car', models.CharField(help_text='Введите класс машины (эконом/бизнес)', max_length=6, verbose_name='Эконом/Бизнес')),
                ('number', models.CharField(help_text='Введите номер машины', max_length=8, unique=True, verbose_name='Номер')),
                ('colour', models.CharField(help_text='Введите цвет машины', max_length=15, verbose_name='Цвет')),
                ('date_of_production', models.TextField(help_text='Введите год выпуска машины', max_length=4, verbose_name='Дата производства')),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=20, verbose_name='Фамилия')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=20, verbose_name='Имя')),
                ('patronymic', models.CharField(help_text='Введите отчество', max_length=20, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(help_text='Введите год рождения', verbose_name='Дата рождения')),
                ('INN', models.DecimalField(decimal_places=0, help_text='Введите ИНН', max_digits=12, unique=True, verbose_name='ИНН')),
                ('passport', models.CharField(help_text='Введите номер и серию паспорта', max_length=11, verbose_name='Паспорт')),
                ('cars', models.ForeignKey(help_text='Введите автомобиль', on_delete=django.db.models.deletion.CASCADE, to='catalog.cars', to_field='number', verbose_name='Автомобили')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(help_text='Введите дату и время заказа', verbose_name='Заказы')),
                ('address_from', models.TextField(help_text='Введите адрес подачи такси', verbose_name='Заказы')),
                ('address_to', models.TextField(help_text='Введите адрес следования', verbose_name='Заказы')),
                ('number_of_passengers', models.DecimalField(decimal_places=0, help_text='Введите количество пассажиров', max_digits=1, verbose_name='Заказы')),
                ('length', models.DecimalField(decimal_places=2, help_text='Введите длину маршрута в километрах', max_digits=6, verbose_name='Заказы')),
                ('drivers', models.ForeignKey(help_text='Введите водителя', on_delete=django.db.models.deletion.CASCADE, to='catalog.drivers', verbose_name='Водители')),
            ],
        ),
    ]
