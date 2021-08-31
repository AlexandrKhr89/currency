from django.shortcuts import render
from django.http import HttpResponse

from currency_1.utils import generate_password as gp

# Crea      te your views here.
def generate_password(request):
    password = gp()
    return HttpResponse(password)

def hello_world(request):
    return HttpResponse('Hello World')