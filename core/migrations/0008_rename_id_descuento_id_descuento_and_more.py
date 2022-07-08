# Generated by Django 4.0.4 on 2022-07-08 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_producto_id_descuento_producto_precio_antiguo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='descuento',
            old_name='id',
            new_name='id_descuento',
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_descuento',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.descuento'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_antiguo',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
