# Generated by Django 2.1.7 on 2019-05-11 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0002_frequencia_ipcom'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='fucionario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.Funcionario'),
        ),
    ]
