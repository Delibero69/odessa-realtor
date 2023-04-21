
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('call/', call,name='call'),
    path('riviera/', riviera,name='riviera'),
    path('call2/', call2,name='call2'),
    path('show_apartment/', show_apartment,name='show_apartment'),
    # path('apartment/<int:Building_id>/', show_apartment, name='show_apartment')

]
