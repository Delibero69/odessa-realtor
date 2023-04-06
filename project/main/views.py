from django.shortcuts import render


def index(request):
    context = {
        'title': 'Купить квартиру',
    }
    return render(request, "main/index.html", context)


def contact(request):
    context = {
        'title': 'Контактная информация жилого района "Сады Ривьеры"',
    }
    return render(request, "main/contact.html", context)


def about(request):
    context = {
        'title': 'Информация о новом жилом районе "Сады Ривьеры"',
    }
    return render(request, "main/about.html", context)


def apartmentsearch(request):
    context = {
        'title': 'Тут вы можете подобрать себе квартиру',
    }
    return render(request, "main/apartmentsearch.html", context)


def call(request):
    context = {
        'title': 'Информация о новом жилом районе "Сады Ривьеры"',
    }
    return render(request, "main/about.html", context)
