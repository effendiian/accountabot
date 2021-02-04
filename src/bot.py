# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$'):
        await handle_command(message)


async def handle_command(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$goodbye'):
        await message.channel.send('No...')

# Run the client.
client.run(TOKEN)



