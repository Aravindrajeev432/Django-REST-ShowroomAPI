# Generated by Django 4.1.4 on 2023-01-12 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0002_carenquiresmodel_delete_carenquires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carenquiresmodel',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('completed', 'completed')], default='pending', max_length=100, null=True),
        ),
    ]
