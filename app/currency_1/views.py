from django.shortcuts import render

from django.shortcuts import get_object_or_404

from currency_1.utils import generate_password as gp

from currency_1.models import Rate

from django.http import HttpResponse


# Create your views here.


def generate_password(request):
    password = gp()
    return HttpResponse(password)


def hello_world(request):
    return HttpResponse('Hello World')


def rate_list(request):
    queryset = Rate.objects.all()
    print(queryset.count())
    print(queryset.query)
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
