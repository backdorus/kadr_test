# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import recipe,ingridient

class recipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_ing' )

admin.site.register(ingridient)
admin.site.register(recipe,recipeAdmin)