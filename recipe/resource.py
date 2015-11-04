from rest_framework import serializers
from .models import ingridient,recipe

class recipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipe
        fields = ('url')