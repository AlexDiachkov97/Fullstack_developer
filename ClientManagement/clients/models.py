from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Client(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('Не в работе', 'Не в работе'),
        ('В работе', 'В работе'),
        ('Отказ', 'Отказ'),
        ('Сделка закрыта', 'Сделка закрыта'),
    ]

    account_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    inn = models.CharField(max_length=12, unique=True)
    responsible_person = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clients')
    status = models.CharField(max_length=50, choices=ACCOUNT_STATUS_CHOICES, default='Не в работе')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'
