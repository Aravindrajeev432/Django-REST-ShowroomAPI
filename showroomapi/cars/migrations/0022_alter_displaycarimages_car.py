# Generated by Django 4.1.4 on 2023-01-13 10:23

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0021_remove_displaycars_images_displaycarimages_car_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaycarimages',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.CharField, related_name='carimg', to='cars.displaycars'),
        ),
    ]
