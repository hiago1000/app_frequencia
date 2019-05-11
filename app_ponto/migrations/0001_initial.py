# Generated by Django 2.1.7 on 2019-05-11 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=70, verbose_name='Cargo do funcionário')),
            ],
        ),
        migrations.CreateModel(
            name='Config_horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_entrada_1', models.TimeField(blank=True, null=True)),
                ('horario_saida_1', models.TimeField(blank=True, null=True)),
                ('horario_entrada_2', models.TimeField(blank=True, null=True)),
                ('horario_saida_2', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario_entrada_1', models.TimeField(null=True)),
                ('horario_saida_1', models.TimeField(null=True)),
                ('horario_entrada_2', models.TimeField(null=True)),
                ('horario_saida_2', models.TimeField(null=True)),
                ('justificativa', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome')),
                ('data_de_nascimento', models.DateTimeField(blank=True, null=True, verbose_name='data de nascimento')),
                ('telefone_celular', models.CharField(blank=True, help_text='Numero de telefone celular no formato (99)99999-9999', max_length=15, null=True, verbose_name='Telefone Celular')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Cargo')),
                ('config_horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Config_horario')),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Funcionario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
    ]
