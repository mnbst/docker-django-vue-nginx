# Generated by Django 2.2.8 on 2020-01-29 14:38

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary_console', '0010_auto_20200125_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caption',
            name='word_imi',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), size=None),
        ),
    ]