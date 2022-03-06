# Generated by Django 4.0.3 on 2022-03-06 02:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('data', models.DateTimeField(default=datetime.datetime(2022, 3, 5, 23, 56, 57, 558926))),
                ('nome_produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='relatorio_dashboard.produto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='relatorio_dashboard.vendedor')),
            ],
        ),
    ]
