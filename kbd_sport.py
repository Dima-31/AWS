import requests
from bs4 import BeautifulSoup
import json
from viberbot.api.messages import KeyboardMessage
from viberbot.api.messages import (
    TextMessage)


from viber.connection import viber_api

cmd_main = "c1_sport"
cmd_sport_v1 = "c10"
cmd_sport_v2 = "c7"

# НАЩ тут локальный список команд. Он будет доклеен к общему списку
all_cmdlist = [cmd_main, cmd_sport_v1, cmd_sport_v2]

_kbd2 = {
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
            "ActionBody": cmd_sport_v1,
            "ReplyType": "message",
            "Text": "Футбол"
        },
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_sport_v2,
            "ReplyType": "message",
            "Text": "Хокей"
        },
    ]
}
MAIN_KEYBOARD = KeyboardMessage(tracking_data='tracking_data', keyboard=_kbd2)


def process(id, msg) -> bool:
    # Мы обрабатываем ТОЛЬКО свои метки и шлем команды. Возвращает True если надо отправить главное меню.
    if msg == cmd_main:
        viber_api.send_messages(id, [TextMessage(text='Какой вид спорта?'), MAIN_KEYBOARD])
        return False

    if msg == cmd_sport_v1:
        viber_api.send_messages(id, [TextMessage(text=sport()+' :)'),])
        return True

    elif msg == cmd_sport_v2:
        viber_api.send_messages(id, [TextMessage(text=sport_2()+' :)')])
        return True


def sport():
    return "новости футбола будут тут"
def sport_2():
    return 'Новости хокея'