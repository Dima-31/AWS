import requests
from viberbot.api.messages import KeyboardMessage
from viberbot.api.messages import (
    TextMessage
)
# опрежедим тут только команды анекдотов

# главная команда во всех файлах одинаковая но импортить будем по разному
from viber.connection import viber_api
cmd_main = "c1_rost"
# под команды тут можно делать как угодно
cmd_rost_v1 = "c8"
cmd_rost_v2 = "c9"
# НАЩ тут локальный список команд. Он будет доклеен к общему списку
all_cmdlist = [cmd_main, cmd_rost_v1, cmd_rost_v2]


kbd3 = {
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
            "ActionBody": cmd_rost_v1,
            "ReplyType": "message",
            "Text": "Отдых на Море"
        },
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_rost_v2,
            "ReplyType": "message",
            "Text": "Отдых в Горах"
        },
    ]
}
MAIN_KEYBOARD = KeyboardMessage(tracking_data='tracking_data', keyboard=kbd3)

def process(id, msg) -> bool:
    # Мы обрабатываем ТОЛЬКО свои метки и шлем команды. Возвращает True если надо отправить главное меню.
    if msg == cmd_main:
        viber_api.send_messages(id, [TextMessage(text='Какой вид отдыха вас интересует?'), MAIN_KEYBOARD])
        return False

    if msg == cmd_rost_v1:
        viber_api.send_messages(id, [TextMessage(text=rost()+' :)'),])
        return True

    elif msg == cmd_rost_v2:
        viber_api.send_messages(id, [TextMessage(text=rost_2()+' :)')])
        return True


def rost():


    return "Пляжи Украины"

def rost_2():
    return 'Горы Украины'