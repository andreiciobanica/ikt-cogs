# -*- coding: utf-8 -*-
from redbot.core import commands


class Notificare(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="blocarechat")
    async def blocarechat(self, ctx):
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await logs_channel.send("Chat-ul a fost blocat de <@" + str(ctx.author.name) + ">)
    
    @commands.command(name="deblocarechat")
    async def deblocarechat(self, ctx):
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=None)
        await logs_channel.send("Chat-ul a fost deblocat!" + str(ctx.author.id))
