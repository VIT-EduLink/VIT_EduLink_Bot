import discord
from discord import app_commands
from discord.ext import commands
import requests

import config

from discord.ui import Button, View

heads = config.admins

class Utility(commands.Cog):
    """ All utility commands should be defined here for the sake for simplicity """
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name="post", description="Send a POST request to an endpoint.")
    @commands.check(lambda ctx: ctx.author.id in heads)
    async def postdata(self, ctx: commands.Context, subject: str, link: str, *, label: str):
        """Send a POST request to the specified endpoint."""
        url = f"{config.API}{subject}"
        data = {"label": label, "link": link}

        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
            await ctx.send("Done")
        except requests.RequestException as e:
            await ctx.send(f"An error occurred while sending the POST request: {str(e)}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")


    @commands.command(name="endpoints", description="Shows list of endpoints.")
    @commands.check(lambda ctx: ctx.author.id in heads)
    async def endpoints(self, ctx: commands.Context):
        """Shows list of endpoints."""
        em = discord.Embed(
            title="List of Endpoints: ",
            description="``` calculus - Calculus endpoint\n\n chem - Engineering Chemistry endpoint\n\n eee - Foundations of Electrical and Electronics Engineering endpoint\n\n beee - Basic Electrical and Electronic Engineering endpoint\n\n bphy - Engineering Physics endpoint\n\n beng - Techincal English Communication endpoint```"
        )
        await ctx.reply(embed = em)

async def setup(bot) -> None:
    await bot.add_cog(Utility(bot))
