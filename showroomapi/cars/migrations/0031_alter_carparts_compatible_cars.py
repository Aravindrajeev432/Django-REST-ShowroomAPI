# Generated by Django 4.1.4 on 2023-01-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0030_alter_cars_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carparts',
            name='compatible_cars',
            field=models.ManyToManyField(to='cars.unipartnumbers'),
        ),
    ]
