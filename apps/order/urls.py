from django.contrib import admin
from django.urls import path
from apps.order.views import *

app_name = 'order'

urlpatterns = [
    path('orders/', orders, name='orders'),
]
