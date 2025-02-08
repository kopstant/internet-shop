from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import home, contact, description

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('description/<int:pk>/', description, name='description'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)