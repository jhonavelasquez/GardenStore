# Generated by Django 4.0.4 on 2022-07-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_suscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='descuento',
            field=models.IntegerField(default=5),
        ),
    ]
