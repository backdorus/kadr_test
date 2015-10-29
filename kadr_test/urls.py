from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from recipe.views import recipeListView

urlpatterns = [
    url(r'^$', recipeListView.as_view(), name='list'),
    url(r'^(?P<slug>\S+)$', recipeListView.as_view(), name="entry_detail"),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
