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
            await message.channel.send('Hello World!')

        if content.startswith('!roll'):
            try:
                operacao = content.split(maxsplit=1)[1]
                try:
                    result = Roller(operacao).result
                    await message.channel.send(f'Resultado: {result}')
                except InvalidOperation:
                    await message.channel.send(f'Rolagem Inválida!')
            except IndexError:
                await message.channel.send(
                    f'Defina a operação da Rolagem! Exemplo: !roll 1d20 + 2'
                )


client = MyClient()
client.run(os.getenv('BOT_TOKEN'))
