# Generated by Django 2.2.6 on 2019-10-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('_id', models.CharField(max_length=500, primary_key=True, serialize=False, unique=True)),
                ('photoName', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=1000, unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]