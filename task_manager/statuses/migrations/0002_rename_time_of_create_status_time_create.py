# Generated by Django 4.2.3 on 2023-07-25 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='time_of_create',
            new_name='time_create',
        ),
    ]
