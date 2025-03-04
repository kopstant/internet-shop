from django.contrib.auth.models import User
from django.db import models
from users.models import CustomUser

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='catalog/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, verbose_name='категория', **NULLABLE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created_at = models.DateField(verbose_name='дата создания', **NULLABLE)
    updated_at = models.DateField(verbose_name='дата последнего изменения', **NULLABLE, )
    publications_flag = models.BooleanField(default=False, verbose_name="Признак публикации(булевое значение)")
    owner = models.ForeignKey(CustomUser, verbose_name='Владелец', help_text='Укажите владельца продукта',
                              **NULLABLE,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.product_name} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = (
            'price',
            'category',
            'created_at',
            'updated_at',
        )
        permissions = (
            ('can_unpublish_product', 'Can unpublish product'),
        )


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('-created_at',)
