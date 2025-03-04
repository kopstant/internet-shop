# Generated by Django 5.1.5 on 2025-01-26 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='превью')),
                ('price', models.IntegerField(verbose_name='цена за покупку')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('updated_at', models.DateField(blank=True, null=True, verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('price', 'category', 'created_at', 'updated_at'),
            },
        ),
    ]
