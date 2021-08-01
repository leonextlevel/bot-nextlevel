import os
import discord
from dotenv import load_dotenv

from roller import Roller

# Carrega as variáveis de ambiente do .env
load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        content = message.content
        print('Message from {0.author}: {0.content}'.format(message))
        if content.startswith("!hello"):
            await message.channel.send('Hello World!')

        if content.startswith('!roll'):
            operacao = content.split(maxsplit=1)[1]
            roller = Roller(operacao)
            await message.channel.send(f'Resultado: {roller.result}')


client = MyClient()
client.run(os.getenv('BOT_TOKEN'))
