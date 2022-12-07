import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.utils import get

from helpers import checks


class RoleColorSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="None", emoji="0️⃣"
            ),
            discord.SelectOption(
                label="Ghastly Green", emoji="1️⃣"
            ),
            discord.SelectOption(
                label="Shallow Yellow", emoji="2️⃣"
            ),
            discord.SelectOption(
                label="Obsolete Orange", emoji="3️⃣"
            ),
            discord.SelectOption(
                label="Breathtaking Blue", emoji="4️⃣"
            ),
            discord.SelectOption(
                label="Marvelous Magenta", emoji="5️⃣"
            ),
            discord.SelectOption(
                label="Lullaby Lavender", emoji="6️⃣"
            ),
            discord.SelectOption(
                label="Retro Red", emoji="7️⃣"
            ),
            discord.SelectOption(
                label="Whitey White", emoji="8️⃣"
            ),
        ]
        super().__init__(
            placeholder="Choose...",
            min_values=1,
            max_values=1,
            options=options,
        )
    async def callback(self, interaction: discord.Interaction):
        choices = {
            "None": 0,
            "Ghastly Green": 1,
            "Shallow Yellow": 2,
            "Obsolete Orange": 3,
            "Breathtaking Blue": 4,
            "Marvelous Magenta": 5,
            "Lullaby Lavender": 6,
            "Retro Red": 7,
            "Whitey White": 8,
        }
        user_choice = self.values[0]

        
        if user_choice == "None":
            role = get(interaction.user.guild.roles, name="Remove")
            role_color = (0x99AAB5)
        elif user_choice == "Ghastly Green":
            role = get(interaction.user.guild.roles, name="Ghastly Green")
            role_color = (0x2ECC71)
        elif user_choice == "Shallow Yellow":
            role = get(interaction.user.guild.roles, name="Shallow Yellow")
            role_color = (0xfeb900)
        elif user_choice == "Obsolete Orange":
            role = get(interaction.user.guild.roles, name="Obsolete Orange")
            role_color = (0xfc7a11)
        elif user_choice == "Breathtaking Blue":
            role = get(interaction.user.guild.roles, name="Breathtaking Blue")
            role_color = (0x0ccfd4)
        elif user_choice == "Marvelous Magenta":
            role = get(interaction.user.guild.roles, name="Marvelous Magenta")
            role_color = (0xac2c96)
        elif user_choice == "Lullaby Lavender":
            role = get(interaction.user.guild.roles, name="Lullaby Lavender")
            role_color = (0xceaffa)
        elif user_choice == "Retro Red":
            role = get(interaction.user.guild.roles, name="Retro Red")
            role_color = (0xf02359)
        elif user_choice == "Whitey White":
            role = get(interaction.user.guild.roles, name="Whitey White")
            role_color = (0xffffff)
        
        result_embed = discord.Embed(color=role_color)
        
        result_embed.set_author(
            name=interaction.user.name,
            icon_url=interaction.user.avatar.url
        )
        
        await interaction.user.remove_roles((get(interaction.user.guild.roles, name="Ghastly Green")), 
            (get(interaction.user.guild.roles, name="Shallow Yellow")),
            (get(interaction.user.guild.roles, name="Obsolete Orange")),
            (get(interaction.user.guild.roles, name="Breathtaking Blue")),
            (get(interaction.user.guild.roles, name="Marvelous Magenta")),
            (get(interaction.user.guild.roles, name="Lullaby Lavender")),
            (get(interaction.user.guild.roles, name="Retro Red")),
            (get(interaction.user.guild.roles, name="Whitey White"))
        )

        if role in interaction.user.roles:
            result_embed.description = f"Removed {role}"
        elif role_color == (0x99AAB5):
            result_embed.description = f"Removed all colors"
        else:    
            await interaction.user.add_roles(role)
            result_embed.description = f"Added {role}"
            

        await interaction.response.edit_message(embed=result_embed, content=None, view=None)
          

class RoleColorSelectView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(RoleColorSelect())


class Misc(commands.Cog, name="Misc"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="rolecolor",
        description="Grants one of the role colors. These roles may be taken away at any time"
    )
    @checks.not_blacklisted()
    async def rolecolor(self, context: Context) -> None:
        """
        Grants one of the role colors. These roles may be taken away at any time.

        :param context: The hybrid command context.
        """
        view = RoleColorSelectView()
        await context.send("Please make your choice", view=view)

    @commands.hybrid_command(
        name="ded",
        description="ded"
    )
    @checks.not_blacklisted()
    async def ded(self, context: Context) -> None:
        """
        ded

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="**d** **e** **d**",
            color=0x65DDB7
        )
        embed.set_image(
            url=("https://media.tenor.com/H1G6O-KvYywAAAAC/the-dancing-dorito-i-revive-this-chat.gif")
        )
        await context.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))
