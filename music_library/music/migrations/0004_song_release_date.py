# Generated by Django 3.2.7 on 2021-09-03 02:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210902_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='release_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]