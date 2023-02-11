# Generated by Django 4.1.4 on 2023-01-30 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0019_baydetails_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="baycurrentjob",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]