import os
import sys
import json

import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Context

from helpers import checks
from helpers.embed import custom_embed


class Disable(commands.Cog, name="disable"):
    def __init__(self, client):
        if not os.path.isfile("config.json"):
            sys.exit("'config.json' not found! Please add it and try again.")
        else:
            with open("config.json") as file:
                config = json.load(file)

        self.client = client
        self.config = config

    @commands.command(
        name="disable",
        description="Disables the email authentification on the server.",
    )
    @checks.is_owner()
    async def disable(self, ctx: Context) -> None:
        with open("state.json", "r") as file:
            state = json.load(file)

        isEnabled = state["isEnabled"]

        if isEnabled:
            self.client.dispatch("change_state", "disable")

            uncheckedRole = discord.utils.get(ctx.guild.roles, name=self.config["uncheckedRoleName"])

            if not uncheckedRole:
                await custom_embed(
                    self.config["basicErrorMessage"],
                    ctx.channel,
                    False,
                )
                return

            perms = discord.Permissions()
            perms.update(
                read_messages=True,
                read_message_history=True,
                connect=True,
                speak=True,
                send_messages=True,
                change_nickname=False,
                view_channel=True,
            )

            # Give all perms to unchecked role
            await uncheckedRole.edit(reason=None, permissions=perms) if uncheckedRole else None

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

            # Delete check channel
            checkChannel = get(ctx.guild.channels, name=self.config["checkChannelName"])

            await checkChannel.delete() if checkChannel else None

            await custom_embed(
                "Bot disabled!",
                ctx.channel,
                True,
            )
        else:
            await custom_embed(
                "Bot is already disabled!",
                ctx.channel,
                False,
            )


async def setup(client):
    await client.add_cog(Disable(client))
