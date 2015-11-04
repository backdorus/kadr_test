from .models import recipe
from django.views.generic import ListView, DetailView
from rest_framework import routers, serializers, viewsets

class recipeListView(ListView):
    model = recipe

class entryDetail(DetailView):
    model = recipe

class RecipeSerializer(viewsets.ModelViewSet):
    class Meta:
        model = recipe
        #fields = ('url', 'name')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = recipe.objects.all()
    serializer_class = RecipeSerializer