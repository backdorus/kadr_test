# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingridients',
            field=models.ManyToManyField(to='recipe.ingridient', verbose_name='\u0418\u043d\u0433\u0440\u0438\u0434\u0438\u0435\u043d\u0442\u044b'),
        ),
    ]
