# Generated by Django 5.0.3 on 2024-04-04 21:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internal_shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(max_length=50)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internal_shop_app.producto')),
            ],
        ),
    ]
