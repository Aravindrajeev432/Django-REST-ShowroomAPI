# Generated by Django 4.1.4 on 2022-12-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_displaycars_chase_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=50)),
            ],
        ),
    ]
