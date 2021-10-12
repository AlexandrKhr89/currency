import random

from currency_1.models import ContactUs
from currency_1.models import Rate
from currency_1.models import SourceBank

from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random data (Rate and ContactUs objects) for HomeWork 6 like DmytroKaminskiy'

    def handle(self, *args, **options):
        # print('Hello from generate_data.py')
        # print('Hello from Rate.objects.create')
        for index in range(10):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=index,
                buy=(random.randint(2000, 2999))/100,
                source=random.choice(('monobank', 'privatbank', 'vkurse')),
            )
        # print('Bay from Rate.objects.create')
        # print('Hello from ContactUs.objects.create')
        for index in range(10):
            ContactUs.objects.create(
                email_from=fake.email(),
                subject=fake.text(max_nb_chars=10),
                message=fake.text(max_nb_chars=100),
                )
        # print('Bay from ContactUs.objects.create')
        # print('Hello from SourceBank.objects.create')
        for index in range(10):
            SourceBank.objects.create(
                name_source=random.choice(('monobank', 'privatbank', 'vkurse')),
                url_source=fake.text(max_nb_chars=100),
                )
        # print('Bay from SourceBank.objects.create')
        # print('Bay from generate_data.py')
