from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import authenticate, get_user_model
Consumer = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):

        Consumer.objects.create_user(
            username='jacob',
            email='jacob@gmail.com',
            password='top_secret'
        )