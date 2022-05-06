import json
import os
import sys

import discord
from discord.ext import commands
from discord.ext.commands import Context
from discord.ui import Button, View

from helpers import checks
from helpers.embed import custom_embed


class Enable(commands.Cog, name="enable"):
    def __init__(self, client):
        if not os.path.isfile("config.json"):
            sys.exit("'config.json' not found! Please add it and try again.")
        else:
            with open("config.json") as file:
                config = json.load(file)

        self.client = client
        self.config = config

    async def handle_click(self, interaction):
        self.client.dispatch("check_click", interaction)

    @commands.command(
        name="enable",
        description="Enables the email authentification on the server.",
    )
    @checks.is_owner()
    async def enable(self, ctx: Context) -> None:
        with open("state.json", "r") as file:
            state = json.load(file)

        isEnabled = state["isEnabled"]

        if not isEnabled:
            self.client.dispatch("setup", ctx.guild)
            self.client.dispatch("change_state", "enable")

            uncheckedRole = discord.utils.get(ctx.guild.roles, name=self.config["uncheckedRoleName"])

            if not uncheckedRole:
                await custom_embed(
                    self.config["basicErrorMessage"],
                    ctx.channel,
                    False,
                )
                return

            # Set check channel perms (only visible from unchecked role)
            overwrites = {
                ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                uncheckedRole: discord.PermissionOverwrite(read_messages=True),
            }

            # Create check channel
            checkChannel = await ctx.guild.create_text_channel(self.config["checkChannelName"], overwrites=overwrites)

            # Set description depending on the extentsions added
            description = self.config["checkChannelMessage"]

            embed = discord.Embed(
                title=f"checkmate | Check Infos",
                description=description,
                color=0xF6E6CC,
            )

            # Create the button
            button = Button(label="Start the check process", emoji="✅")

            button.callback = self.handle_click

            view = View()
            view.add_item(button)

            # Send the message in check channel
            await checkChannel.send(embed=embed, view=view)

            await custom_embed(
                "Bot enabled!",
                ctx.channel,
                True,
            )
        else:
            await custom_embed(
                "Bot is already enabled!",
                ctx.channel.id,
                False,
            )


def setup(client):
    client.add_cog(Enable(client))
