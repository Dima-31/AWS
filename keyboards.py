from viberbot.api.messages import KeyboardMessage
# Импортировал команды и обработчик команд
from .kbd_anekdot import all_cmdlist as anek_cmdlist, cmd_main as cmd_anekdot
from .kbd_sport import all_cmdlist as sport_cmdlist, cmd_main as cmd_sport
from .kbd_rost import all_cmdlist as  rost_cmdlist, cmd_main as  cmd_rost
cmd_main = "c2"
cmd_rost_v1 = "c1,1"
cmd_rost_v2 = "c2,2"


all_cmdlist = []
# добавил команды анекдотов
all_cmdlist.extend(anek_cmdlist)
all_cmdlist.extend(sport_cmdlist)
all_cmdlist.extend(rost_cmdlist)

SAMPLE_KEYBOARD = {
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
            "ActionBody": cmd_sport,
            "ReplyType": "message",
            "Text": "Спорт"
        },
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_rost,
            "ReplyType": "message",
            "Text": "Отдых"
        },
        {
            "Columns": 2,
            "Rows": 1,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": cmd_anekdot,
            "ReplyType": "message",
            "Text": "Анекдоты"
        },
    ]
}
START_KEYBOARD = KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD)

