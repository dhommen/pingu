import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello ' + message.author.name)

    if message.content.startswith('$bye'):
        await message.channel.send('Bye ' + message.author.name)

    if message.content.startswith('$adventure'):
        await message.channel.send('Hello ' + message.author.name + ' your epic adventure will start soon!')

client.run(os.environ('TOKEN'))