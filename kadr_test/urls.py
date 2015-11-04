from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from recipe.views import recipeListView,entryDetail,UserViewSet



urlpatterns = [
    url(r'^$', recipeListView.as_view(), name='list'),
    url(r'^(?P<slug>\S+)$', entryDetail.as_view(), name="entry_detail"),
    url(r'^api/$', UserViewSet.as_view),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)