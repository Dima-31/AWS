from viberbot.api.bot_configuration import BotConfiguration
from viberbot import Api

bot_configuration = BotConfiguration(
	name='DimaM',
	avatar='http://viber.com/avatar.jpg',
	auth_token=('4bbd4cad75e7ddcd-e98a3adeb8710de5-5cd1130cf994a98c')
)
viber_api = Api(bot_configuration)