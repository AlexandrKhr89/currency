"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from currency_1.views import bank_details
from currency_1.views import bank_list
from currency_1.views import generate_password
from currency_1.views import hello_world
from currency_1.views import rate_create
from currency_1.views import rate_delete
from currency_1.views import rate_details
from currency_1.views import rate_list
from currency_1.views import rate_update

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('gen-pass/', generate_password),

    path('hello_world/', hello_world),

    path('currency_1/rate/list/', rate_list),

    path('currency_1/rate/details/<int:pk>/', rate_details),

    path('currency_1/bank/list/', bank_list),

    path('currency_1/bank/details/<int:pk>/', bank_details),

    path('currency_1/rate/create/', rate_create),

    path('currency_1/rate/update/<int:pk>/', rate_update),

    path('currency_1/rate/delete/<int:pk>/', rate_delete),
]
