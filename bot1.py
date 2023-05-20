import discord

TOKEN = 'xxxx'
print('hello')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('!hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('!hi'):
        await message.channel.send('Hello!')


client.run(TOKEN)
