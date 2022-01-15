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
        roles = [440955056750198795, 865215495623934012, 865215437531512842, 865215444150648853, 865215457672822815, 865215465290334278, 865215472979279872, 865215480600199188, 865215487864078357, 865215503320481812, 865215450883555338, 885152622842101790, 899760338436780042, 892118179269210152, 908442214047293450, 918482495975084092, 920324660997001227, 929494693585227856, 929489148987981824, 929489154079871008, 865215430662291496, 865215510265331712, 865215521094631435, 865215533573341184]
        
        if any(item in ctx.guild.get_role(roles) for item in ctx.author.roles):
            await ctx.message.author.send("item")
            
    #@commands.command(name="tester", pass_context=True)
    #async def grade(self, ctx, user: discord.Member):
       # role = 440955056750198795
       # if ctx.guild.get_role(role) in ctx.author.roles:
        #    await ctx.message.author.send(role)
            
