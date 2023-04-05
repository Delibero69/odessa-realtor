
from django.urls import path
from main.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('order_a_call/', call, name='call'),
    path('apartmentsearch/', apartmentsearch, name='apartmentsearch'),
]