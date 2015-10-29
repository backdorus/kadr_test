# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20151029_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingridient',
            name='id',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='id',
        ),
        migrations.AddField(
            model_name='ingridient',
            name='slug',
            field=models.SlugField(primary_key=True, default=b'SOME STRING', serialize=False, max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(primary_key=True, default=b'SOME STRING', serialize=False, max_length=250, unique=True),
        ),
    ]
