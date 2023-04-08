from django.shortcuts import render

def index(request):
    context = {
        'title': 'Купить квартиру',
    }
    return render(request, "main/index.html", context)


def call(request):
    return render(request, 'main/call.html',)

def show_apartment(request):
    return render(request, 'main/show_apartment.html', )


