# Generated by Django 2.2.6 on 2019-10-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photorepo', '0003_auto_20191017_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.CharField(max_length=1000),
        ),
    ]