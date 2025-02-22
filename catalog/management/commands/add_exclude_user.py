from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Creates the "Product Moderator" group and assigns permissions'

    def handle(self, *args, **kwargs):
        # Создаем группу
        group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Получаем разрешения
        content_type = ContentType.objects.get_for_model(Product)
        can_unpublish = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
        delete_product = Permission.objects.get(codename='delete_product', content_type=content_type)

        # Назначаем разрешения группе
        group.permissions.add(can_unpublish, delete_product)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и права назначены'))