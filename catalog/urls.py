from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, \
    ProductDeleteView, ContactListView, ContactCreateView, category_product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('contact/', ContactListView.as_view(), name='contact_list'),
    path('contact_create/', ContactCreateView.as_view(), name='contact_create'),
    path('category/<int:category_id>/', category_product_list, name='category_product_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
