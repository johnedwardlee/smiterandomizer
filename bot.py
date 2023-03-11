import os

import discord
import smiterandomizer
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        msg = str(message.content).lower()
        if msg.startswith('!smitrand teams'):
            await message.reply(smiterandomizer.smitRandom(input='teams'))
        if msg.startswith('!smitrand mage'):
            await message.reply(smiterandomizer.smitRandom(input='mage'))
        if msg.startswith('!smitrand warrior'):
            await message.reply(smiterandomizer.smitRandom(input='warrior'))
        if msg.startswith('!smitrand guardian'):
            await message.reply(smiterandomizer.smitRandom(input='guardian'))
        if msg.startswith('!smitrand hunter'):
            await message.reply(smiterandomizer.smitRandom(input='hunter'))
        if msg.startswith('!smitrand assassin'):
            await message.reply(smiterandomizer.smitRandom(input='assassin'))
        if msg.startswith('!smitrand help'):
            await message.reply(smiterandomizer.smitRandom(input=None))


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)