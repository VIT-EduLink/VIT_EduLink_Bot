import discord
from discord.ui import Button, View
from discord import app_commands
from discord.ext import commands
TOKEN = "XXXXXXXXXX"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print("Link established")


#UI for all subs

BEEE = Button(label="BEEE", style=discord.ButtonStyle.blurple)
BEEE_link1 =  Button(label="Link1", style=discord.ButtonStyle.gray, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

CHEM = Button(label="Chemistry", style=discord.ButtonStyle.blurple)

ENPH = Button(label="Engineering Physics", style=discord.ButtonStyle.blurple)

CALC = Button(label="Calculus", style=discord.ButtonStyle.blurple)

#interaction
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!sub"):
        view = View()
        view.add_item(BEEE)
        view.add_item(CHEM)
        view.add_item(ENPH)
        view.add_item(CALC)

        async def button_callback(interaction):
            viewBEEE = View()
            viewBEEE.add_item(BEEE_link1)
            await interaction.channel.send('Available PDFs are :', view = viewBEEE)
            await interaction.response.defer()
        BEEE.callback =button_callback

        await message.channel.send('Available subjects are :', view = view)



client.run(TOKEN)
