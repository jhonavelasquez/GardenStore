# Generated by Django 4.0.4 on 2022-07-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_descuento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('codigo', models.IntegerField(max_length=5, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.IntegerField(max_length=20)),
                ('fecha', models.DateField()),
                ('imagen', models.CharField(default='imagen', max_length=400)),
            ],
        ),
    ]
