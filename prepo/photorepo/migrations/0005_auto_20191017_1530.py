# Generated by Django 2.2.6 on 2019-10-17 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photorepo', '0004_auto_20191017_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='_id',
            new_name='pid',
        ),
    ]
