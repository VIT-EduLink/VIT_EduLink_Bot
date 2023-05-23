import discord
from discord import app_commands
from discord.ext import commands

from views.buttons import Subjects #Importing subjects class from buttons.py containing buttons and links 

class SlashCmd(commands.Cog):
    """ All slash commands should be defined here for the sake for simplicity """
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="subjects", description="displays available subjects")
    async def subject_commands(self, interaction: discord.Interaction) -> None:
        """ Displays available subjects """
        await interaction.response.send_message("Available subjects are: ", view=Subjects())

async def setup(bot) -> None:
  await bot.add_cog(SlashCmd(bot))
