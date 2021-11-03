# currency

'~/currency$ python3 -m venv env'

'~/currency$ . env/bin/activate'

'$ pip freeze > requirements.txt'

'$ python manage.py runserver'

'$ sudo apt install sqlite'

'$ python manage.py makemigrations'

'$ python manage.py migrate'

'$ python manage.py showmigrations'

'$ flake8 app/'

'$ pip install django-extensions'

'$ pip install ipython'

'$ python ./app/manage.py shell_plus --print-sql'

'~/currency$ python ./app/manage.py generate_data'

'~/currency$ python ./app/manage.py generate_data --help'

'$ python ./app/manage.py shell_plus --print-sql'

'In [1]: Rate.objects.count()'

'In [5]: Rate.objects.filter(sale=1).count()'

'In [6]: Rate.objects.filter(sale__gt=1).count()'

'In [7]: Rate.objects.filter(source__startswith='m').count()'

'In [9]: Rate.objects.filter(source__endswith='k').count()'

'In [10]: Rate.objects.filter(source__contains='m').count()'

'In [11]: Rate.objects.filter(sale__gt=1, buy__gt=1).count()'

'In [12]: from django.db.models import Q'

'In [13]: Rate.objects.filter(Q(sale__gt=1) | Q(buy__gt=1)).count()'

'In [2]: Rate.objects.filter(Q(sale__gt=1) & Q(buy__gt=1)).count()'

'In [3]: Rate.objects.filter(~Q(sale__gt=1) & Q(buy__gt=1)).count()'


**Динамическая сборка условий фильтрации:**

'In [5]: q = Q(sale__gt=1)'

'In [6]: q |= q(buy__gt=1)'

'In [8]: Rate.objects.filter(q).count()'

'In [12]: rates = Rate.objects.all()'

'In [14]: rates = rates.exclude(type='usd')'

'In [15]: for rate in rates:
    ...:     pass
    ...:'

'In [16]: for rate in rates:
    ...:     print(rate)
    ...:'

**Sort**

'In [17]: Rate.objects.order_by('sale')'

'In [17]: Rate.objects.order_by('-sale')'

'In [19]: Rate.objects.order_by('-sale', 'id')'

**Random sort**

'In [20]: Rate.objects.order_by('?')'

'In [5]: ContactUs.objects.create(email_from='Faker.email()', subject='Faker().currency()', message='Faker().text(max_nb_chars=200)',)'

'$ git status'

'$ git branch'

'$ git branch myNewBranch'

'$ git checkout Home_Work_6'

'$ git add --all'

'$ git commit -m 'Add Home_Work_7'

'$ git push origin Home_Work_7'

**Lesson 8**

'$ python ./app/manage.py runserver'

'In [1]: Rate.objects.all()[:100]'

'In [3]: Rate.objects.all()[:100].values_list('id')'

'In [4]: Rate.objects.all()[:100].values_list('id', flat=True)'

'In [1]: SourceBank.objects.all()'

'In [2]: SourceBank.objects.all().values_list('id')'

'In [3]: SourceBank.objects.all().values_list('name_source')'

'In [4]: SourceBank.objects.all().values_list('url_source')'

**Lesson 9**

'Makefile'

'(env) alexandr89@DESKTOP-L9M6OAB:~/currency$ make runserver'

'$ ifconfig'

'$ make runserver'

'$ pip install django-annoying'



