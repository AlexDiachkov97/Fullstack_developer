from django.core.management.base import BaseCommand
from clients.models import Client, CustomUser
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Создание пользователей
        user1 = CustomUser.objects.create(
            username='ivanov',
            password=make_password('password1'),
            full_name='Иванов Иван Иванович'
        )
        user2 = CustomUser.objects.create(
            username='petrov',
            password=make_password('password2'),
            full_name='Петров Петр Петрович'
        )
        user3 = CustomUser.objects.create(
            username='sidorov',
            password=make_password('password3'),
            full_name='Сидоров Сидор Сидорович'
        )

        # Создание клиентов
        Client.objects.create(
            last_name='Иванов',
            first_name='Иван',
            middle_name='Иванович',
            birth_date='1980-01-01',
            inn='123456789012',
            responsible_person=user2,
            status='Не в работе'
        )
        Client.objects.create(
            last_name='Петров',
            first_name='Петр',
            middle_name='Петрович',
            birth_date='1985-05-15',
            inn='234567890123',
            responsible_person=user3,
            status='Не в работе'
        )
        Client.objects.create(
            last_name='Сидоров',
            first_name='Сидор',
            middle_name='Сидорович',
            birth_date='1990-07-20',
            inn='345678901234',
            responsible_person=user1,
            status='Не в работе'
        )
