import discord 
from discord import app_commands 
from discord.ext import commands 

class Subjects(discord.ui.View): 
    """ This class contains all the subject button views """

    @discord.ui.button(label='BEEE', style=discord.ButtonStyle.blurple)
    async def BEEE(self, interaction: discord.Interaction, button: discord.ui.Button):
        resource = Resources()
        resource.add_item(resource.BEEE_link1)
        resource.add_item(resource.BEEE_link2)
        resource.add_item(resource.BEEE_link3)
        resource.add_item(resource.BEEE_link4)
        await interaction.response.send_message("`[BEEE]` Available PDFs are: ", view=resource)

    @discord.ui.button(label='Chemistry', style=discord.ButtonStyle.blurple)
    async def CHEM(self, interaction: discord.Interaction, button: discord.ui.Button):
        resource = Resources()
        resource.add_item(resource.CHEM_link1)
        resource.add_item(resource.CHEM_link2)
        resource.add_item(resource.CHEM_link3)
        resource.add_item(resource.CHEM_link4)
        await interaction.response.send_message("`[CHEMISTRY]` Available PDFs are: ", view=resource)
        
    @discord.ui.button(label='Engineering Physics', style=discord.ButtonStyle.blurple)
    async def ENPH(self, interaction: discord.Interaction, button: discord.ui.Button):
        resource = Resources()
        resource.add_item(resource.ENPH_link1)
        resource.add_item(resource.ENPH_link2)
        resource.add_item(resource.ENPH_link3)
        resource.add_item(resource.ENPH_link4)
        await interaction.response.send_message("`[ENPH]` Available PDFs are: ", view=resource)

    @discord.ui.button(label='Calculus', style=discord.ButtonStyle.blurple)
    async def CALC(self, interaction: discord.Interaction, button: discord.ui.Button):
        resource = Resources()
        resource.add_item(resource.CALC_link1)
        resource.add_item(resource.CALC_link2)
        resource.add_item(resource.CALC_link3)
        resource.add_item(resource.CALC_link4)
        await interaction.response.send_message("`[CALCULUS]` Available PDFs are: ", view=resource)

class Resources(discord.ui.View):
    """ This class contains all the pdf links (for now its rickroll but in future it will be fetching requests from backend API) """
    #BEEE Links
    BEEE_link1= discord.ui.Button(label='Link1', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    BEEE_link2= discord.ui.Button(label='Link2', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    BEEE_link3= discord.ui.Button(label='Link3', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    BEEE_link4= discord.ui.Button(label='Link4', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    #CHEM Links
    CHEM_link1= discord.ui.Button(label='Link1', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CHEM_link2= discord.ui.Button(label='Link2', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CHEM_link3= discord.ui.Button(label='Link3', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CHEM_link4= discord.ui.Button(label='Link4', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    #ENPH Links
    ENPH_link1= discord.ui.Button(label='Link1', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ENPH_link2= discord.ui.Button(label='Link2', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ENPH_link3= discord.ui.Button(label='Link3', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    ENPH_link4= discord.ui.Button(label='Link4', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    #CALC Links
    CALC_link1= discord.ui.Button(label='Link1', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CALC_link2= discord.ui.Button(label='Link2', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CALC_link3= discord.ui.Button(label='Link3', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    CALC_link4= discord.ui.Button(label='Link4', style=discord.ButtonStyle.link, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
