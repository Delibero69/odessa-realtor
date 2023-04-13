from django.urls import path
from .views import *

urlpatterns = [
    path('', docindex,name='docindex'),
    path('reconstruction/', reconstruction, name='reconstruction')
]