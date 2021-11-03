from annoying.functions import get_object_or_None

from currency_1.forms import RateForm
from currency_1.models import Rate
from currency_1.models import SourceBank
from currency_1.utils import generate_password as gp

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render


# Create your views here.


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello World')


def rate_list(request):
    queryset = Rate.objects.all()
    # print(queryset.count())
    # print(queryset.query)
    # print(rate.id)

    # ids = []
    #
    # for rate in queryset:
    #     ids.append(rate.id)

    # from time import time

    context = {
        # 'message': f'Hello From context: {time()}',
        'objects': queryset,
    }

#     html =f"""
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#
# <h1>
# {ids}
# </h1>
#
# </body>
# </html>
# """

    # return HttpResponse(str(ids))
    # return HttpResponse(html)
    return render(request, 'rate_list.html', context=context)


def rate_details(request, pk):
    # http://127.0.0.1:8000/rate/details/?id=109
    # google: django path parametrs
    # id_ = request.GET['id']
    # rate = Rate.objects.get(id=id_)
    try:
        rate = Rate.objects.get(pk=pk)
    except Rate.DoesNotExist:
        # rate = None
        raise Http404(f"Poll does not exist with {pk}")

    rate = get_object_or_404(Rate, pk=pk)
    context = {
        # 'message': f'Hello From context rate_details',,
        'object': rate,
    }

    # return HttpResponse('rate_details')
    return render(request, 'rate_details.html', context=context)


def bank_list(request):
    banks_queryset = SourceBank.objects.all()
    context = {
        'context': 'Hello From bank_list context (views.py)',
        'objects': banks_queryset,
    }
    return render(request, 'bank_list.html', context=context)


def bank_details(request, pk):
    # google: django path parametrs
    try:
        bank = SourceBank.objects.get(pk=pk)
    except SourceBank.DoesNotExist:
        raise Http404(f"Poll does not exist with {pk}")

    bank = get_object_or_404(SourceBank, pk=pk)

    context = {
        'context': 'Hello From bank_details context (views.py)',
        'object': bank,
    }

    return render(request, 'bank_details.html', context=context)


def rate_create(request):
    form_data = request.GET
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        # print('breakpoint() from views.py')
        # breakpoint()
        if form.is_valid():
            print('YES, VALID')
            form.save()
            return HttpResponseRedirect('/currency_1/rate/list')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'message': 'Hello From rate_create context (views.py)',
        'form': form,
        'count': Rate.objects.count(),
    }
    # breakpoint()
    return render(request, 'rate_create.html', context=context)


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)
    # context = {
    #     'message': 'Hello From rate_update context (views.py)',
    #     'instance': instance,
    # }
    #
    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            print('YES, VALID')
            form.save()
            return HttpResponseRedirect('/currency_1/rate/list')
    elif request.method == 'GET':
        form = RateForm(instance=instance)

    context = {
        # 'message': 'Hello From rate_update context (views.py)',
        'form': form,
        # 'count': Rate.objects.count(),
    }
    # breakpoint()
    return render(request, 'rate_update.html', context=context)


def rate_delete(request, pk):
    # instance = get_object_or_404(Rate, pk=pk)
    instance = get_object_or_None(Rate, pk=pk)
    if instance is not None:
        instance.delete()
    return HttpResponseRedirect('/currency_1/rate/list')
