from django.urls import path
from .views import *

urlpatterns = [
    path('', docindex,name='docindex'),
]