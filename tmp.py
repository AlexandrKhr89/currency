import random
from faker import Faker
fake = Faker()
# print(random.choice(('monobank', 'privatbank', 'vkurse')))
# print((random.randint(2000, 2999))/100)

# print(fake.name())
# print(fake.email())
# print(fake.job())
# print(fake.currency())
# print(fake.text(max_nb_chars=200))

for index in range(100):
        email_from = f'{fake.email()}'
        subject = f'{fake.text(max_nb_chars=20)}'
        message = f'{fake.text(max_nb_chars=50)}'
        print(email_from)
        print(subject)
        print(message)