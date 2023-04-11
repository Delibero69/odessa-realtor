from django.urls import path
from .views import *


urlpatterns = [
    path('oformleniye-prava-sobstvennosti/', oformleniye, name = 'oformleniye'),
]