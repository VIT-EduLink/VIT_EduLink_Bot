import discord
from discord.ui import Button, View
from discord import app_commands
TOKEN = "xxxxxxxxxxxxxxxxxxxxxx"
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#UI for all subs

BEEE = Button(label="BEEE", style=discord.ButtonStyle.blurple)
BEEE_link1 =  Button(label="Link1", style=discord.ButtonStyle.gray, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

CHEM = Button(label="Chemistry", style=discord.ButtonStyle.blurple)

ENPH = Button(label="Engineering Physics", style=discord.ButtonStyle.blurple)

CALC = Button(label="Calculus", style=discord.ButtonStyle.blurple)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1109016227210350634))
    print("Edulink established!")


@tree.command(name = "subjects", description = "displays available subjects", guild=discord.Object(id=1109016227210350634))
async def first_command(interaction,):
    view = View()
    view.add_item(BEEE)
    view.add_item(CHEM)
    view.add_item(ENPH)
    view.add_item(CALC)
    await interaction.response.send_message('Available subjects are :', view=view)
    async def button_callback(interaction):
        viewBEEE = View()
        viewBEEE.add_item(BEEE_link1)
        await interaction.response.send_message('Available PDFs are :', view=viewBEEE)

    BEEE.callback = button_callback

client.run(TOKEN)
