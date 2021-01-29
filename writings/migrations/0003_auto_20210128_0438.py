# Generated by Django 3.1.5 on 2021-01-28 04:38

import datetime
from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('writings', '0002_auto_20210127_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='date',
            field=django_cryptography.fields.encrypt(models.DateField(default=datetime.date.today, verbose_name='Date')),
        ),
    ]