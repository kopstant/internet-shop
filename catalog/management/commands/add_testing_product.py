from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from datetime import date


class Command(BaseCommand):
    help = 'Adds a test product to the database'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории
        electronics = Category.objects.create(category_name="Электроника", description="Техника и гаджеты")
        clothing = Category.objects.create(category_name="Одежда", description="Модная одежда")
        books = Category.objects.create(category_name="Книги", description="Литература и учебники")

        # Создаем продукты
        products = [
            {
                "product_name": "Смартфон",
                "description": "Мощный смартфон",
                "price": 500,
                "category": electronics,
                "created_at": date(2023, 10, 1),
                "updated_at": date(2023, 10, 1),
            },
            {
                "product_name": "Ноутбук",
                "description": "Игровой ноутбук",
                "price": 1200,
                "category": electronics,
                "created_at": date(2023, 10, 1),
                "updated_at": date(2023, 10, 1),
            },
            {
                "product_name": "Футболка",
                "description": "Хлопковая футболка",
                "price": 20,
                "category": clothing,
                "created_at": date(2023, 10, 1),
                "updated_at": date(2023, 10, 1),
            },
            {
                "product_name": "Роман",
                "description": "Классический роман",
                "price": 15,
                "category": books,
                "created_at": date(2023, 10, 1),
                "updated_at": date(2023, 10, 1),
            },
        ]

        for data in products:
            Product.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Тестовые продукты успешно добавлены!'))
