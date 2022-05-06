import os
import sys
import json

import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Context

from helpers import checks
from helpers.embed import custom_embed


class Leave(commands.Cog, name="leave"):
    def __init__(self, client):
        if not os.path.isfile("config.json"):
            sys.exit("'config.json' not found! Please add it and try again.")
        else:
            with open("config.json") as file:
                config = json.load(file)

        self.client = client
        self.config = config

    @commands.command(
        name="leave",
        description="Proper way to kick the bot.",
    )
    @checks.is_owner()
    async def leave(self, ctx: Context) -> None:
        # Delete check channel
        checkInfosChannel = get(ctx.guild.channels, name=self.config["checkChannelName"])

        await checkInfosChannel.delete() if checkInfosChannel else None

        # Delete checked & unchecked roles
        uncheckedRole = get(ctx.guild.roles, name=self.config["uncheckedRoleName"])
        checkedRole = get(ctx.guild.roles, name=self.config["checkedRoleName"])

        await uncheckedRole.delete() if uncheckedRole else None
        await checkedRole.delete() if checkedRole else None

        for role in ctx.guild.roles:
            # Reset all perms for default role
            if role.name == "@everyone":
                perms = discord.Permissions()
                perms.update(
                    read_messages=True,
                    read_message_history=True,
                    connect=True,
                    speak=True,
                    send_messages=True,
                    change_nickname=True,
                    view_channel=True,
                )
                await role.edit(reason=None, permissions=perms)

        await custom_embed(
            self.config["leaveMessage"],
            ctx.channel,
            True,
        )

        await ctx.guild.leave()


def setup(client):
    client.add_cog(Leave(client))
