from django.shortcuts import render


def index(request):
    context = {
        'title': 'Купить квартиру',
    }
    return render(request, "main/index.html", context)


def contact(request):
    context = {
        'title': 'Контактная информация для связи с нами',
    }
    return render(request, "main/contact.html", context)


