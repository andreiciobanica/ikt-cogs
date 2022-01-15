# -*- coding: utf-8 -*-
from redbot.core import commands
from datetime import datetime, timedelta, timezone
from pytz import timezone
import discord

class lideri_grade(commands.Cog):

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(pass_context=True)
    @commands.command(name="grade")
    async def grade(self, ctx, user: discord.Member):
        role = 440955056750198795
        if ctx.guild.get_role(role) in ctx.author.roles:
            await ctx.message.author.send(role)
            
