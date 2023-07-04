# Generated by Django 4.2.2 on 2023-07-03 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('copies', '0001_initial'),
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='copy',
            name='loans',
            field=models.ManyToManyField(related_name='loan_copies', through='loans.Loan', to='copies.copy'),
        ),
    ]