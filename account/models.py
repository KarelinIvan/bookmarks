from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Profile(models.Model):
    """ Модель профиля """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_of_birth = models.DateField(**NULLABLE, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Profile for {self.user.username}'
