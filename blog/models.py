from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое", **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)
    publications_flag = models.BooleanField(default=False, verbose_name="Признак публикации(булевое значение)")
    numbers_of_posts = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f'{self.title}, {self.content[:20]}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at', 'publications_flag', 'numbers_of_posts']
