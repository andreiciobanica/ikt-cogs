# -*- coding: utf-8 -*-
from redbot.core import commands
from datetime import datetime, timedelta, timezone
from pytz import timezone
import discord

class Notificare(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.mod()
    @commands.command(name="blocarechat")
    async def blocarechat(self, ctx):
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        tz = timezone("Europe/Bucharest")
        embed = discord.Embed(title="Blocare chat 🤫", color=0xefe125)
        embed.add_field(name="NUME", value="ID", inline=True)
        embed.add_field(name=str(ctx.author.name), value=str(ctx.author.id), inline=True)
        embed.set_footer(text=str(datetime.now(tz).strftime("%d %B %Y %H:%M:%S")))
        await logs_channel.send(embed=embed)
    
    @commands.mod()
    @commands.command(name="deblocarechat")
    async def deblocarechat(self, ctx):
        channel = self.bot.get_channel(440957219593519126)
        logs_channel = self.bot.get_channel(715676435372834927)
        await channel.set_permissions(ctx.guild.default_role, send_messages=None)
        tz = timezone("Europe/Bucharest")
        embed = discord.Embed(title="Deblocare chat 🤫", color=0xefe125)
        embed.add_field(name="NUME", value="ID", inline=True)
        embed.add_field(name=str(ctx.author.name), value=str(ctx.author.id), inline=True)
        embed.set_footer(text=str(datetime.now(tz).strftime("%d %B %Y %H:%M:%S")))
        await logs_channel.send(embed=embed)
