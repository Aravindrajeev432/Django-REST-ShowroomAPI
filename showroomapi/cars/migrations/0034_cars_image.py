# Generated by Django 4.1.4 on 2023-01-28 14:24

import cars.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0033_alter_cars_uni_car_part_num_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cars",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=cars.models.CarNameFile,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "webp"]
                    )
                ],
            ),
        ),
    ]
