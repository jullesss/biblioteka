# Generated by Django 4.2.2 on 2023-07-04 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 22, 9, 24, 415435, tzinfo=datetime.timezone.utc)),
        ),
    ]
