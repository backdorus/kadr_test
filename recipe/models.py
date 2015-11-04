# -*- coding: utf-8 -*-
from django.db import models

class ingridient(models.Model):
    name = models.CharField(verbose_name = u'Ингридиент',max_length=30, unique=True)
    slug = models.SlugField(verbose_name = u'URL',primary_key=True, max_length=250, unique=True, default='SOME STRING')
    def __unicode__(self):
        return self.name

class recipe(models.Model):
    name = models.CharField(verbose_name = u'Рецепт',max_length=30,unique=True)
    ingridients = models.ManyToManyField(ingridient, verbose_name=u'Ингридиенты')
    slug = models.SlugField(verbose_name = u'URL',primary_key=True, max_length=250, unique=True, default='SOME STRING')

    def get_ing(obj):
        return ','.join(obj.ingridients.values_list('name', flat=True))
    get_ing.short_description = 'Ингридиенты'

    def __unicode__(self):
        return self.name
