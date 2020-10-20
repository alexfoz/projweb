# Generated by Django 3.1.1 on 2020-10-16 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=8)),
                ('nome', models.CharField(max_length=80)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=14)),
                ('dataDeNascimento', models.DateField(max_length=10)),
                ('dataDeAdmissao', models.DateField(max_length=10)),
                ('dataDeTermino', models.DateField(null=True)),
                ('matricula', models.CharField(max_length=8)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo.cargo')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]