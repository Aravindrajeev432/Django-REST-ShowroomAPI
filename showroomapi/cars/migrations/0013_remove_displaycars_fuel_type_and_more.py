# Generated by Django 4.1.4 on 2022-12-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_fueltype_geartype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='displaycars',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='displaycars',
            name='gear_type',
        ),
        migrations.AddField(
            model_name='displaycars',
            name='fuel_type',
            field=models.ManyToManyField(to='cars.fueltype'),
        ),
        migrations.AddField(
            model_name='displaycars',
            name='gear_type',
            field=models.ManyToManyField(to='cars.geartype'),
        ),
    ]
