from django.db import models
from django.conf import settings
from user.models import NULLABLE


class Form(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    ATTRACTION = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="user")

    name = models.CharField(max_length=100, verbose_name='name')
    surname = models.CharField(max_length=100, verbose_name='surname')

    image = models.ImageField(verbose_name='image')
    about = models.CharField(max_length=1000, verbose_name='about')

    country = models.CharField(max_length=100, verbose_name='country')
    city = models.CharField(max_length=100, verbose_name='city')
    birth_date = models.DateField(verbose_name='birth_date')
    attraction = models.CharField(choices=ATTRACTION, verbose_name='attraction')

    def __str__(self):
        return f'Form({self.name}).'

    class Meta:
        verbose_name = 'form'
        verbose_name_plural = 'forms'
        ordering = ('name',)

