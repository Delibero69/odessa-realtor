from django.shortcuts import render

# Create your views here.

def docindex(requests):
    return render(requests, 'documents/base.html')


def reconstruction(requests):
    return render(requests, 'documents/reconstruction.html')