from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0, verbose_name='Баланс')

    def __str__(self):
        return self.user.username


class Orders(models.Model):
    user_id = models.CharField(max_length=200, null=True, blank=True, verbose_name='ID пользователя')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Юзернейм')
    amount = models.FloatField(default=0, verbose_name='Сумма')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес')
    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return str(self.user_id)