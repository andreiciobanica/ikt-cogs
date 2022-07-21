# -*- coding: utf-8 -*-
import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class permisiuni(commands.Cog):

    politie = [
        999442129162092584,
        999448089515544646,
        999450217231425759,
        999449616007303299,
        999449808437792788,
        999442532331175968,
        999442625172099132,
        999441568975048874,
        999441660838674442
    ]
    
    # diicot = [
    #     999442143171072090,
    #     999448152971169942,
    #     999450505363333214,
    #     999449634449653891,
    #     999449765051908186,
    #     999443232062722089,
    #     999443241759944764,
    #     999441768917512233,
    #     999445368469201016
    # ]
    # smurd = [
    #     999442153388376074,
    #     999448727766970498,
    #     999450517405171793,
    #     999449241573396540,
    #     999449785968885840,
    #     999443269203271722,
    #     999443278254575656,
    #     999441826316566628,
    #     999441833614651412
    # ]

    politierol = [
        999493803218046976,
        999452220242272326,
        999452219059478588,
        999452217654382615,
        999452332045648023,
        999452380812820511,
        999452220397465742,
        999452211312590978,
        999455078194876496,
        999438314656510075
    ]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="permisiuni")
    async def permisiuni(self, ctx):
        manager = 999558907800322141
        everyone = ctx.guild.default_role
        for x in permisiuni.politie:
            c = self.bot.get_channel(x)
            i = permisiuni.politie.index(x)
            if i != 7 and i != 8:
                await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
                await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
                await c.set_permissions(ctx.guild.get_role(999564403403931698), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
                await c.set_permissions(ctx.guild.get_role(999493801448054794), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            if i == 0 or i == 1 or i == 3 or i == 4:
                for y in permisiuni.politierol:
                    await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            elif i==7 or i==8:
                await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
                await c.set_permissions(ctx.guild.get_role(999564403403931698), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
                await c.set_permissions(ctx.guild.get_role(999493801448054794), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
                await c.set_permissions(everyone, view_channel=True, manage_channels=False, manage_permissions=None, create_instant_invite=None, connect=None, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            else:
                for y in permisiuni.politierol:
                    await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
