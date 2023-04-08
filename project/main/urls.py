
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('call/', call,name='call'),
    # path('contact/', contact,name='contact'),
]
