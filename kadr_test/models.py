from django.db import models

class Ingridient(models.Model):
    name = models.CharField(verbose_name = u'Ингридиент',max_length=30, unique=True)

class Recipe(models.Model):
    name = models.CharField(verbose_name = u"Рецепт",max_length=30,unique=True)
    ingridients = models.ManyToManyField(Ingridient)



