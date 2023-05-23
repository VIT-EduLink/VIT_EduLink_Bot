'''
[ARCHIVED] - For future reference
'''
# Basic outline about the idea of the working. 
# It uses normal reactions but due the limit of 9 reactions per message we dropped the idea.
# It was better approach to switch to buttons instead

import discord

TOKEN = 'xxxxxxxxxxxxxx'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

subjects = ">>> Available subs:\n1. BEEE \n2. Engineering Calculus \n3. Chemistry \n "

@client.event
async def on_message(message):

    if message.content.startswith('!hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('!subs'):
        sub = await message.channel.send(subjects)
        await sub.add_reaction("1️⃣")
        await sub.add_reaction("2️⃣")
        await sub.add_reaction("3️⃣")
        await sub.add_reaction("4️⃣")


    if message.author == client.user:
        return

client.run(TOKEN)
