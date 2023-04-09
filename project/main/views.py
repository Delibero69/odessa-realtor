from django.shortcuts import render
from .forms import ContactForm
import asyncio
from telegram import Bot
from telegram.ext import Updater, MessageHandler
from django.conf import settings
loop = asyncio.get_event_loop()



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
            # Отправка данных в Telegram
            message = f'Name: {name}\nPhone Number: {phone_number}'

            async def send_telegram_message():
                # Замените на ваш токен бота
                bot = Bot(token='6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc')

                # Замените на ваш Chat ID
                chat_id = '-1001920393262'

                # Текст сообщения

                # Отправка сообщения
                await bot.send_message(chat_id=chat_id, text=message)
            loop.run_until_complete(send_telegram_message())

            return render(request, 'main/index.html')
        else:
            return render(request, 'main/call.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'main/call.html', {'form': form})

def show_apartment(request):
    return render(request, 'main/show_apartment.html', )


