import discord
import os
import random

pinguinFacts = ['All 17 species of penguins are found exclusively in the Southern Hemisphere.',
'Emperor Penguins are the tallest species, standing nearly 4 feet tall. The smallest is the Little Blue Penguin, which is only about 16 inches.',
'The fastest species is the Gentoo Penguin, which can reach swimming speeds up to 22 mph.',
'A penguins striking coloring is a matter of camouflage; from above, its black back blends into the murky depths of the ocean. From below, its white belly is hidden against the bright surface.',
'Fossils place the earliest penguin relative at some 60 million years ago, meaning an ancestor of the birds we see today survived the mass extinction of the dinosaurs.',
'Penguins ingest a lot of seawater while hunting for fish, but a special gland behind their eyes—the supraorbital gland—filters out the saltwater from their blood stream. Penguins excrete it through their beaks, or by sneezing.',
'Unlike most birds—which lose and replace a few feathers at a time—penguins molt all at once, spending two or three weeks land-bound as they undergo what is called the catastrophic molt.',
'All but two species of penguins breed in large colonies of up to one thousand birds.',
'It varies by species, but many penguins will mate with the same member of the opposite sex season after season.',
'Similarly, most species are also loyal to their exact nesting site, often returning to the same rookery in which they were born.',
'Some species create nests for their eggs out of pebbles and loose feathers. Emperor Penguins are an exception: They incubate a single egg each breeding season on the top of their feet. Under a loose fold of skin is a featherless area with a concentration of blood vessels that keeps the egg warm.',
'In some species, it is the male penguin which incubates the eggs while females leave to hunt for weeks at a time. Because of this, pudgy males—with enough fat storage to survive weeks without eating—are most desirable.',
'Penguin parents—both male and female—care for their young for several months until the chicks are strong enough to hunt for food on their own.',
'If a female Emperor Penguins baby dies, she will often "kidnap" an unrelated chick.',
'Despite their lack of visible ears, penguins have excellent hearing and rely on distinct calls to identify their mates when returning to the crowded breeding grounds.',
'The first published account of penguins comes from Antonio Pigafetta, who was aboard Ferdinand Magellans first circumnavigation of the globe in 1520. They spotted the animals near what was probably Punta Tombo in Argentina. (He called them "strange geese.")',
'An earlier, anonymous diary entry from Vasco da Gamas 1497 voyage around the Cape of Good Hope makes mention of flightless birds as large as ducks.',
'Because they arent used to danger from animals on solid ground, wild penguins exhibit no particular fear of human tourists.',
'Unlike most sea mammals—which rely on blubber to stay warm—penguins survive because their feathers trap a layer of warm air next to the skin that serves as insulation, especially when they start generating muscular heat by swimming around.',
'In the 16th century, the word penguin actually referred to great auks (scientific name: Pinguinus impennis), a now-extinct species that inhabited the seas around eastern Canada. When explorers traveled to the Southern Hemisphere, they saw black and white birds that resembled auks, and called them penguins.']

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

    if message.content.startswith('$penguin'):
        await message.channel.send(pinguinFacts[random.randint(0,19)])

client.run(os.getenv('TOKEN'))