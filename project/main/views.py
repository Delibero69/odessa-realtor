from django.shortcuts import render, HttpResponseRedirect
from .forms import ContactForm
from telegram import Bot
from django.conf import settings
import requests
import urllib

def index(request):
    context = {
        'title': 'Купить квартиру',
    }
    return render(request, "main/index.html", context)


def call(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            def repl(name):
                return name.replace(" ", "_")
            name1 = repl(name)
            bot = Bot(token='6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc')
            chat_id = '-1001920393262'  # Ваш чат айди
            message = f'Name:{name1}'
            message1 = f'PhoneNumber:{phone_number}'
            get_url = urllib.request.urlopen('https://api.telegram.org/bot6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc/sendMessage?chat_id=-1001920393262&text=' + message)
            get_url1 = urllib.request.urlopen('https://api.telegram.org/bot6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc/sendMessage?chat_id=-1001920393262&text=' + message1)
            # bot.send_message(chat_id=-1001920393262, text=name1)
            return render(request, 'main/index.html')
        else:
            form = ContactForm()
            return render(request, 'main/call.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'main/call.html', {'form': form})
