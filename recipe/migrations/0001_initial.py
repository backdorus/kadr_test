# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingridient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u0418\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442')),
            ],
        ),
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='\u0420\u0435\u0446\u0435\u043f\u0442')),
                ('ingridients', models.ManyToManyField(to='recipe.ingridient')),
            ],
        ),
    ]
