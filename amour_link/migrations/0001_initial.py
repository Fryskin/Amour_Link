# Generated by Django 4.2.7 on 2024-01-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('surname', models.CharField(max_length=100, verbose_name='surname')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('about', models.CharField(max_length=1000, verbose_name='about')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('birth_date', models.DateField(verbose_name='birth_date')),
                ('attraction', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], verbose_name='attraction')),
            ],
            options={
                'verbose_name': 'form',
                'verbose_name_plural': 'forms',
                'ordering': ('name',),
            },
        ),
    ]
