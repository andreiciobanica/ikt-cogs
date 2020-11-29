# -*- coding: utf-8 -*-
from redbot.core import commands


class Notificare(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="blocarechat")
    async def blocarechat(self, ctx):
        permissions = PermissionOverwrite()
        permissions.send_messages = False
        channel = client.get_channel(440957219593519126)
        await channel.set_permissions(guild.default_role, overwrite=permissions)
    
    @commands.command(name="deblocarechat")
    async def blocarechat(self, ctx):
        permissions = PermissionOverwrite()
        permissions.send_messages = None
        channel = client.get_channel(440957219593519126)
        await channel.set_permissions(guild.default_role, overwrite=permissions)