# Generated by Django 3.1.2 on 2020-10-18 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
        ('usuario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuariot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataUltimaAlteracao', models.DateField(max_length=10)),
                ('solicitado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ticketId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickets')),
            ],
        ),
    ]
