from django.db import models


class User(models.Model):
    name = models.CharField(max_length=300, verbose_name='Name')
    surname = models.CharField(max_length=300, verbose_name='Surname')
    phone = models.CharField(max_length=25, verbose_name='Phone')
    email = models.EmailField(max_length=255, verbose_name='Email')

    def __str__(self):
        return self.name
