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

    @commands.command(name="colider", pass_context=True)
    async def grade(self, ctx, user: discord.Member):
        roles = [
            ctx.guild.get_role(440955056750198795),
            ctx.guild.get_role(865215495623934012),
            ctx.guild.get_role(865215437531512842),
            ctx.guild.get_role(865215444150648853),
            ctx.guild.get_role(865215457672822815),
            ctx.guild.get_role(865215465290334278),
            ctx.guild.get_role(865215472979279872),
            ctx.guild.get_role(865215480600199188),
            ctx.guild.get_role(865215487864078357),
            ctx.guild.get_role(865215503320481812),
            ctx.guild.get_role(865215450883555338),
            ctx.guild.get_role(885152622842101790),
            ctx.guild.get_role(899760338436780042),
            ctx.guild.get_role(892118179269210152),
            ctx.guild.get_role(908442214047293450),
            ctx.guild.get_role(918482495975084092),
            ctx.guild.get_role(920324660997001227),
            ctx.guild.get_role(929494693585227856),
            ctx.guild.get_role(929489148987981824),
            ctx.guild.get_role(929489154079871008),
            ctx.guild.get_role(865215430662291496)
            ]
        
        for x in roles:
            for y in ctx.author.roles:
                if x==y:
                    await ctx.message.author.send(roles.index(x))
            
    #@commands.command(name="tester", pass_context=True)
    #async def grade(self, ctx, user: discord.Member):
       # role = 440955056750198795
       # if any(item in roles for item in ctx.author.roles):
        #    await ctx.message.author.send(role)
            
