# Generated by Django 3.1.2 on 2020-10-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ferias',
            name='fim',
            field=models.DateField(max_length=20),
        ),
        migrations.AlterField(
            model_name='ferias',
            name='inicio',
            field=models.DateField(max_length=20),
        ),
    ]
