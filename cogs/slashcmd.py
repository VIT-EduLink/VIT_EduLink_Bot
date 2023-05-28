import discord
from discord import app_commands
from discord.ext import commands
import requests

import config

from discord.ui import Button, View

class SlashCmd(commands.Cog):
    """ All slash commands should be defined here for the sake for simplicity """
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="subjects", description="displays available subjects")
    async def subject_commands(self, interaction: discord.Interaction) -> None:
        """ Displays available subjects """
        await interaction.response.defer()
        response = requests.get(config.API)
        if response.status_code == 200:
            subjects_data = response.json()

            category_labels = {
                "cseData": "CSE",
                "chemData": "Chemistry",
            }

            view = View()
            for category, subjects in subjects_data.items():
                display_label = category_labels.get(category, category)  # Get display label, use category if not found
                button = Button(style=discord.ButtonStyle.blurple, label=display_label)
                button.callback = lambda i, b=button, s=subjects: self.button_callback(i, b, s)
                view.add_item(button)

            await interaction.followup.send("Available subjects are:", view=view)
        else:
            await interaction.followup.send("Failed to retrieve subjects data from the API.")

    async def button_callback(self, interaction: discord.Interaction, button: Button, subjects) -> None:
        view = View()
        for subject in subjects:
            label = subject['label']
            link = subject['link']
            sub_button = Button(style=discord.ButtonStyle.link, label=label, url=link)
            view.add_item(sub_button)

        await interaction.response.send_message(f"Subjects for {button.label}:", view=view)

async def setup(bot) -> None:
    await bot.add_cog(SlashCmd(bot))