# Generated by Django 4.0.4 on 2022-07-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_historial_imagen_remove_historial_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='codigo',
            field=models.IntegerField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
