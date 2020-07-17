
import json
import requests  # Добавим Библиотеку для отправки запросов
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from viberbot.api.messages import (
    TextMessage
)
# Вынесли отдельно чтоб было удобно использовать
from .connection import viber_api

from viber.keyboards import START_KEYBOARD, all_cmdlist,  START_KEYBOARD, cmd_rost, cmd_rost_v1, cmd_rost_v2



def main_page(request):
    return render(request,'index.html',)
auth_token = '4bbd4cad75e7ddcd-e98a3adeb8710de5-5cd1130cf994a98c'
url = 'https://chatapi.viber.com/pa/send_message'
headers = {'X-Viber-Auth-Token': auth_token}
# ДЕКОРАТОР ДЛЯ функций и отправки
def sending(func):
    def wrapped(*args):
        return requests.post(url, json.dumps(func(*args)), headers=headers)
    return wrapped
# Отправка текста
@sending
def send_text(agent: object, text: object, track: object = None) -> object:
    m = dict(receiver=agent, min_api_version=2, tracking_data=track, type="text", text=text)
    return m
#отправка файла
@sending
def send_file(agent, text, track=None):
    m = dict(receiver=agent, min_api_version=2, tracking_data=track, type="file", text=text)
    return m
@csrf_exempt
def trx_bot(request, a1=None):
    if request.method == "POST":
        viber = json.loads(request.body.decode('utf-8'))
        print(viber)
        if viber['event'] == 'conversation_started':
            id = viber['sender']['id']
            viber_api.send_messages(id, [
                TextMessage(text='Рады видеть!'),START_KEYBOARD
            ])
        elif viber['event'] == 'webhook':
            #print(viber)
            #print("Webhook успешно установлен")
            return HttpResponse(status=200)
        elif viber['event'] == 'message':
           id = viber['sender']['id']
           msg = viber['message']['text']
           # если полученный текст есть в списке команд
           if msg in all_cmdlist:
               exect_cmd(id,msg)
           else:
               viber_api.send_messages(id, [TextMessage(text='Ваша команда не найдена'), START_KEYBOARD])
           send_text(id,a1)
        else:
            # print("Это не Webhook - пробуй еще раз, или используй POSTMAN")
            return HttpResponse(status=200)
        return HttpResponse(status=200)

def exect_cmd(id,message):
    # импортируем обработчики клавиатур из каждого файла.
    from .kbd_anekdot import  process as anek_process
    from .kbd_sport import process as sport_process
    from .kbd_rost import process as rost_process

    # применяем все обработчики
    if anek_process(id, message):
        # Вернуло тру значит отправим еще и главное меню.
        viber_api.send_messages(id, [START_KEYBOARD, ])

    if sport_process(id, message):
        # Вернуло тру значит отправим еще и главное меню.
        viber_api.send_messages(id, [START_KEYBOARD, ])

    if rost_process(id, message):
        # Вернуло тру значит отправим еще и главное меню.
        viber_api.send_messages(id, [START_KEYBOARD, ])

    # viber_api.send_messages(id, [TextMessage(text=message), START_KEYBOARD])


