import requests
from viberbot.api.messages import KeyboardMessage
from viberbot.api.messages import (
    TextMessage
)
# опрежедим тут только команды анекдотов

# главная команда во всех файлах одинаковая но импортить будем по разному
from viber.connection import viber_api

cmd_main = "c3"
# под команды тут можно делать как угодно
cmd_anekdot_v1 = "c4"
cmd_anekdot_v2 = "c5"
# НАЩ тут локальный список команд. Он будет доклеен к общему списку
all_cmdlist = [cmd_main, cmd_anekdot_v1, cmd_anekdot_v2]

_kbd1 =  {
    "Type": "keyboard",
    "Buttons": [
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_anekdot_v1,
            "ReplyType": "message",
            "Text": "Анекдоты про Вовочку"
        },
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_anekdot_v2,
            "ReplyType": "message",
            "Text": "Анекдоты про животных"
        },
       ]

}
MAIN_KEYBOARD =KeyboardMessage(tracking_data='tracking_data', keyboard=_kbd1)

def process(id, msg) -> bool:
    # Мы обрабатываем ТОЛЬКО свои метки и шлем команды. Возвращает True если надо отправить главное меню.
    if msg == cmd_main:
        viber_api.send_messages(id, [TextMessage(text='Какой анекдот?'), MAIN_KEYBOARD])
        return False

    if msg == cmd_anekdot_v1:
        viber_api.send_messages(id, [TextMessage(text=anekdot()+' :)' +'(crazy)'),])
        return True

    elif msg == cmd_anekdot_v2:
        viber_api.send_messages(id, [TextMessage(text=anekdot()+' :)' +'(crazy)')])
        return True

def anekdot():
    url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"
    headers = {
        'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com",
        'x-rapidapi-key': "b81b9712afmshe70e87630759d95p195281jsnf2f0ac57be82",
        'accept': "application/hal+json"
    }
    response = requests.request("GET", url, headers=headers)
    red1 = (response.json())
    return red1['value']
def anekdot_2():
    url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"
    headers = {
        'x-rapidapi-host': "matchilling-tronald-dump-v1.p.rapidapi.com",
        'x-rapidapi-key': "b81b9712afmshe70e87630759d95p195281jsnf2f0ac57be82",
        'accept': "application/hal+json"
    }
    response = requests.request("GET", url, headers=headers)
    red1 = (response.json())
    return red1['value']
