import os
import discord
from dotenv import load_dotenv

from roller import Roller
from roller.exceptions import InvalidOperation

# Carrega as variáveis de ambiente do .env
load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        content = message.content
        print('Mensagem de {0.author}: {0.content}'.format(message))
        if content.startswith("!hello"):
            await message.reply('Hello World!')

        if content.startswith('!roll'):
            try:
                operacao = content.split(maxsplit=1)[1]
                try:
                    roller = Roller(operacao)
                    await message.reply(
                        roller.get_success_message()
                    )
                except InvalidOperation:
                    await message.reply(Roller.get_error_message())
            except IndexError:
                await message.reply(Roller.get_error_message())


client = MyClient()
client.run(os.getenv('BOT_TOKEN'))
