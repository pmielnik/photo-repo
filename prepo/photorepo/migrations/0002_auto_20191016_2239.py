# Generated by Django 2.2.6 on 2019-10-16 22:39

from django.db import migrations, models
import photorepo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('photorepo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(storage=photorepo.storage.PhotoStorage(), upload_to=''),
        ),
    ]