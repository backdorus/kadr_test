from .models import recipe
from django.views.generic import ListView

class recipeListView(ListView):
    model = recipe