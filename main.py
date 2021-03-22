import discord
import os
import random

axolotlFacts = ['Axolotl have an astonishing ability to regenerate body organs and lost limbs.',
'Axolotl can regrow the same limb up to 5 times. Then it stops.',
'The feathery looking branches that extend from either side of its head are its gills.',
'The Axolotl is also over 1,000 times more resistant to cancer than mammals.',
'Axolotl are only be found in Mexico.',
'This Axolotl does not chew its food, it feeds by using suction.',
'As a bottom feeder, the Axolotl makes good use of gravel that gets sucked up with food.',
'Although critically endangered, the Axolotl has very few predators.',
'The Axolotl anatomy has a very unique characteristic, known as neoteny.',
'The word Axolotl comes from the Ancient Aztecs who revered them, and translates to mean ‘water dog’.',
'The Mexican walking fish male and female are easy to identify.',
'The breeding season for the Axolotl is early in the calendar year.',
'The breeding ritual includes a dance.',
'The female Axolotl lays a massive amount of eggs in a protective cover.',
'Aztecs in ancient Mexico used to dine on these fish viewing them as a delicacy that was not only considered to be a rare treat, but they were also consumed for nutritional purposes.',
'Sadly, the Axolotl is classed as critically endangered on the IUCN Red List.',
'Researchers are encouraging Axolotl to breed by building ‘shelters’ in Xochimilco.']

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
    
    if message.content.startswith('$axolotl'):
        await message.channel.send(axolotlFacts[random.randint(0,16)])

client.run(os.getenv('TOKEN'))