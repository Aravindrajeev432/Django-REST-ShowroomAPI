# Generated by Django 4.1.4 on 2023-01-22 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_services_car_alter_services_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='finished_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
