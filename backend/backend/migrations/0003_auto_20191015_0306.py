# Generated by Django 2.2.6 on 2019-10-15 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20191015_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name',
            new_name='_id',
        ),
    ]
