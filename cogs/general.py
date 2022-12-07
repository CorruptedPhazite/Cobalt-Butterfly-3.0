""""
Copyright © Krypton 2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
This is a template to create your own discord bot in python.

Version: 5.3
"""

import platform
import random

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="build",
        description="Cobalt Build & Configuration Info",
    )
    @checks.not_blacklisted()
    async def build(self, context: Context) -> None:
        """
        Cobalt Build & Configuration Info.
        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            color=0x65DDB7
        )
        embed.set_author(
            name="Current Cobalt Build Info",
            url="https://github.com/hecksalmonids/cobalt-cluster/tree/#{current_branch}",
            icon_url='https://cdn.discordapp.com/attachments/753163837057794176/805998319251882034/467450365055336448.png'
        )
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/804750275793518603/819294692608442418/cobalt_icon_2.png"
            )
        embed.add_field(
            name="Parameters",
            value="""Repo: [hecksalmonids/cobalt-cluster](#{remote_repo_url})
                  Branch: [#{current_branch}](https://github.com/hecksalmonids/cobalt-cluster/tree/#{current_branch})
                  Run Mode: #{run_mode}
                  Auto-Updater Present: #{auto_updater_enabled}
                  Python Version: {platform.python_version()}
                  Cogs Loaded: \n```#{active_cogs}```
                  Slash Commands Enabled: #{slash_enabled}
                  Legacy Prefix Commands Enabled: #{prefix_enabled}
                  Prefix: #{self.bot.config['prefix']}
                  Prefix Enabled for Maintinence Commands: #{maint_prefix_enabled}""",
            inline=False
        )
        embed.add_field(
            name="Current Version",
            value="""Commit: [#{commit_hash}](https://github.com/hecksalmonids/cobalt-cluster/commit/#{commit_hash_full})
                  Commit Author: [#{author_name}](https://github.com/#{author_name})
                  Commit Date: #{author_date}
                  Last Update Attempt: #{last_pull_attempted}
                  Update Check Frequency: #{auto_updater_frequency}
                  Time Until Next Update Check:""",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {context.author}"
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="Checks Cobalt's response time",
    )
    @checks.not_blacklisted()
    async def ping(self, context: Context) -> None:
        """
        Checks the Cobalt's response time

        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="**P** **O** **N** **G**",
            description=f"{round(self.bot.latency * 1000)}ms",
            color=0x65DDB7
        )
        await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(General(bot))
