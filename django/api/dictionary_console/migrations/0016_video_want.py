# Generated by Django 3.0.6 on 2020-05-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_console', '0015_auto_20200509_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='want',
            field=models.BooleanField(default=False),
        ),
    ]