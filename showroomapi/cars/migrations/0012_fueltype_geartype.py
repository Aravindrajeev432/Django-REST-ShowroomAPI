# Generated by Django 4.1.4 on 2022-12-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_remove_displaycars_colour_displaycars_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GearType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gear_type', models.CharField(max_length=50)),
            ],
        ),
    ]