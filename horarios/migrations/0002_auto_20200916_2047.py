# Generated by Django 3.1.1 on 2020-09-16 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='horarios',
            old_name='nomeHorario',
            new_name='Horario',
        ),
    ]
