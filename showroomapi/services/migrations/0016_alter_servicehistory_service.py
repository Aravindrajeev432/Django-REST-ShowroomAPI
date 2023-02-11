# Generated by Django 4.1.4 on 2023-01-27 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0015_alter_services_status_servicehistory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicehistory",
            name="service",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="service_log",
                to="services.services",
            ),
        ),
    ]
