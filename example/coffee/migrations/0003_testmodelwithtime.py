# Generated by Django 3.1.5 on 2021-01-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20201205_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelWithTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
