from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        u1 = User.objects.filter(email='ivan@site.ru').first()
        if not u1:
            u1 = User.objects.create_user(
                username='ivan@site.ru',
                first_name='Иван',
                last_name='Иванов',
                email='ivan@site.ru',
                password='1111'
            )
            u1.save()

        u2 = User.objects.filter(email='alex@site.ru').first()
        if not u2:
            u2 = User.objects.create_user(
                username='alex@site.ru',
                first_name='Алексей',
                last_name='Алексеев',
                email='alex@site.ru',
                password='1111'
            )
            u2.save()
