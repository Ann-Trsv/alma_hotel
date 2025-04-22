from django.db import models
from django.contrib.auth.models import AbstractUser


# Переименовываем модель пользователя во избежание конфликтов
class Employee(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('receptionist', 'Ресепшен'),
        ('housekeeping', 'Горничная'),
        ('manager', 'Менеджер'),
        ('employee', 'Сотрудник'),
    ]

    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES, default='employee')
    phone = models.CharField('Телефон', max_length=20, blank=True, null=True)

    # Убираем конфликтующие поля из базовой модели
    username = models.CharField('Логин', max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.get_full_name() or self.username


class Guest(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    passport_number = models.CharField('Номер паспорта', max_length=20, unique=True)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Гость'
        verbose_name_plural = 'Гости'

    def __str__(self):
        return self.full_name


class RoomType(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    base_price = models.DecimalField('Базовая цена', max_digits=10, decimal_places=2)
    max_guests = models.IntegerField('Макс. гостей')

    class Meta:
        verbose_name = 'Тип номера'
        verbose_name_plural = 'Типы номеров'

    def __str__(self):
        return self.name


class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступен'),
        ('occupied', 'Занят'),
        ('maintenance', 'На обслуживании'),
        ('cleaning', 'Уборка'),
    ]

    room_number = models.CharField('Номер комнаты', max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, verbose_name='Тип номера', on_delete=models.CASCADE)
    floor = models.IntegerField('Этаж')
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='available')

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return f"{self.room_number} ({self.room_type.name})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Подтверждено'),
        ('checked_in', 'Заселен'),
        ('checked_out', 'Выселен'),
        ('cancelled', 'Отменено'),
    ]

    guest = models.ForeignKey(Guest, verbose_name='Гость', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name='Номер', on_delete=models.CASCADE)
    check_in_date = models.DateField('Дата заезда')
    check_out_date = models.DateField('Дата выезда')
    booking_date = models.DateTimeField('Дата бронирования', auto_now_add=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='confirmed')
    total_price = models.DecimalField('Общая стоимость', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

    def __str__(self):
        return f"{self.guest} - {self.room}"


class Service(models.Model):
    name = models.CharField('Название услуги', max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class GuestService(models.Model):
    booking = models.ForeignKey(Booking, verbose_name='Бронирование', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE)
    quantity = models.IntegerField('Количество', default=1)
    date = models.DateField('Дата оказания')

    class Meta:
        verbose_name = 'Услуга гостя'
        verbose_name_plural = 'Услуги гостей'

    def __str__(self):
        return f"{self.booking} - {self.service}"


class Payment(models.Model):
    METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Карта'),
        ('online', 'Онлайн'),
    ]

    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('completed', 'Завершено'),
        ('failed', 'Ошибка'),
    ]

    booking = models.ForeignKey(Booking, verbose_name='Бронирование', on_delete=models.CASCADE)
    amount = models.DecimalField('Сумма', max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField('Дата платежа', auto_now_add=True)
    method = models.CharField('Способ оплаты', max_length=20, choices=METHOD_CHOICES)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='completed')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'

    def __str__(self):
        return f"{self.booking} - {self.amount}"