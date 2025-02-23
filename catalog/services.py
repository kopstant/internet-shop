from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHES_ENABLED


def get_products_from_cache():
    """Получает данные по продуктам из кэша, если кэш пуст - получает данные из БД."""
    if not CACHES_ENABLED:
        return Product.objects.all()

    key = "product_list"
    products = cache.get(key)

    if products is None:
        # Получаем продукты из БД и сохраняем в кэш
        products = Product.objects.all()
        cache.set(key, products, timeout=1800) # Cохраняем на 30 минут.
    return products


def list_products_in_category(category):
    """Cервисная функция для работы с продуктами, которая возвращает список всех продуктов в указанной категории."""
    return Product.objects.filter(category=category, publications_flag=True)
