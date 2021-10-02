import random

from currency_1.models import ContactUs
from currency_1.models import Rate


from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random data (Rate and ContactUs objects) for HomeWork 6 like DmytroKaminskiy'

    def handle(self, *args, **options):
        print('Hello from generate_data.py')
        print('Hello from Rate.objects.create')
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=index,
                buy=(random.randint(2000, 2999))/100,
                source=random.choice(('monobank', 'privatbank', 'vkurse')),
            )
        print('Bay from Rate.objects.create')
        print('Hello from ContactUs.objects.create')
        for index in range(100):
            ContactUs.objects.create(
                email_from=f'{fake.email()}',
                subject=f'{fake.text(max_nb_chars=10)}',
                message=f'{fake.text(max_nb_chars=100)}',
                )
        print('Bay from ContactUs.objects.create')
        print('Bay from generate_data.py')
