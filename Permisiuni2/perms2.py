# -*- coding: utf-8 -*-
import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class permisiuni_imperial(commands.Cog):

    logs_toti = [
        874180409913655296, # ban-unban
        899795579406782465, # jail-unjail
        899811976455266304, # kick
        899813253805375488, # clear-chat
        901677591889596428, # warns
        889903660384002048, # player-drop
        932066407909322812, # grade
        932033338347245628, # somaj
        932333705802973184  # f-r
        ]

    logs_only_high = [
        874179720156151898, # add-group
        874180012679528509, # give-money
        872487107715792956, # logs
        885487769508511744, # chocohax-logs
        865215132782166027, # mixas-main
        885487935116431410, # choco-main
        865215133432414219, # mixas-blacklist-key
        885488187391234068, # choco-explo
        885488481487433758  # chat-choco
        ]

    roluri = [
        865215597247594517, #Full Acces //0
        865215596164284426, #Fondator Comunitate //1
        885846054547890197, #Developer //2
        865215595205492766, #Fondator //3
        877214428846772304, #Co-Fondator //4
        865215581162438677, #Supervizor //5
        865215580343631882, #Head of Staff //6
        865215598139801600, #Semi-acces //7
        865215577550094356, #Head of Mod //8
        865215574392963082, #Head of Helpers //9
        865215582046388255, #Manager //10
        925389310423863396, #SA //11
        865215578972880936, #A //12
        865215576287871006, #MOD AV. //13
        865215575265116210, #Mod //14
        913819149736747039, #Helper AV //15
        913818779144831056, #Helper //16
        865215571825131560, #Helper in TESTE //17
        865215570843533332, #STAFF IMPERIAL //18
        941758011414831225, #PC-CHECKER //19
        ]
    
    regulament = [
        883883166765551618, #Server
        900303004568260638, #Jafuri
        865215138709504000, #Discord
        865215209999040512, #Staff
        865215142811140166, #War
        909634465796612096, #Lideri
        941720177068875776, #Sindicat
        865215210938957844  #Sanctiuni
    ]
    
    important = [
        865215144447049749, #ip-anunturi
        865215145688694835, #ip-updates
        865215151736750100, #ip-youtube
        865215226277003334, #ip-server
        865645173181513738  #invite-link
    ]


    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="permisiuniIMP")
    async def permisiuniIMP(self, ctx):
        civil = 907588821091221546
        muted = 892836101117587456
        everyone = ctx.guild.default_role
        for x in permisiuni_imperial.logs_toti:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
        
        for x in permisiuni_imperial.logs_only_high:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
                
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

            for i in range(1, 7):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            for i in range(7, 20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=False, attach_files=False, add_reactions=False, use_external_emojis=False, mention_everyone=False, manage_messages=False, read_message_history=False, send_tts_messages=False, use_slash_commands=None)
        
        for x in permisiuni_imperial.regulament:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 20):
                 await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni_imperial.important:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 10):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            for i in range(10, 20):
                 await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
