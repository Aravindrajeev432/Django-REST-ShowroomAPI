# Generated by Django 4.1.4 on 2023-01-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_serviceinfo_universal_car_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceinfo',
            name='afterwards_service_km',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serviceinfo',
            name='afterwards_service_month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
