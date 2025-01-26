from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
