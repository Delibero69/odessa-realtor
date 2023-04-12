from django.shortcuts import render
from .forms import ContactForm,ContactForm2
import asyncio
from telegram import Bot

from .models import *


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
                chat_id = '-1001920393262'
                await bot.send_message(chat_id=chat_id, text=message)
            loop.run_until_complete(send_telegram_message())

            return render(request, 'main/index.html')
        else:
            return render(request, 'main/call.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'main/call.html', {'form': form})


# def call2(request):
#     if request.method == 'POST':
#         form = ContactFormsTwo(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             content = form.cleaned_data['content']
#             # Отправка данных в Telegram
#             message = f'Name: {name}\nPhone Number: {phone_number}\n\n{content}'
#             async def send_telegram_message():
#                 # Замените на ваш токен бота
#                 bot = Bot(token='6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc')
#                 chat_id = '-1001920393262'
#                 await bot.send_message(chat_id=chat_id, text=message)
#             loop.run_until_complete(send_telegram_message())
#
#             return render(request, 'main/index.html')
#         else:
#             return render(request, 'main/index.html', {'form': form})
#     else:
#         form = ContactFormsTwo()
#         return render(request, 'main/index.html', {'form': form})




async def send_telegram_message(message):
    bot = Bot(token='6160065485:AAFJ7j6U7xApViYEDhBpEB2iCIEOo8vB3Bc')
    chat_id = '-1001920393262'
    await bot.send_message(chat_id=chat_id, text=message)

def call2(request):
    if request.method == 'POST':
        form = ContactForm2(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            content = form.cleaned_data['content']
            # Отправка данных в Telegram
            message = f'Name: {name}\nPhone Number: {phone_number}\n\n{content}'
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_telegram_message(message))
            return render(request, 'main/index.html')
    else:
        form = ContactForm2()
    return render(request, 'main/index.html', {'form': form})




def show_apartment(request, category_id=None):

    apartment = Building.objects.all()
    context = {'apartment': apartment,
               'title':"Купить квартиру"
               }
    return render(request, 'main/show_apartment.html', context)



# def show_apartment(request):
#     return render(request, 'main/show_apartment.html', )

# def show_apartment(request, category_id=None):
#     apartment = Building.objects.get(category_id=category_id)
#     context = {'apartment': apartment,
#                'title':"Купить Квартиру"
#                }
#     return render(request, 'main/show_apartment.html', context)