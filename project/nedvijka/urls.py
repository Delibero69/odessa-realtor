from django.conf import settings
from django.urls import path
from main.views import *


from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     path('', index, name='index'),
#     path('contact/', contact, name='contact'),
#     path('about/', about, name='about'),
#     path('order_a_call/', call, name='call'),
#     path('apartmentsearch/', apartmentsearch, name='apartmentsearch'),
# ]