# Generated by Django 4.1.4 on 2023-01-03 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_displaycars_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='displaycars',
            name='type',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback')], max_length=50, null=True),
        ),
    ]