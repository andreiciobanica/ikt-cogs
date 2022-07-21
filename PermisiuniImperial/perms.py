# -*- coding: utf-8 -*-
import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class permisiuni(commands.Cog):

#     politie = [
#         999442129162092584,
#         999448089515544646,
#         999450217231425759,
#         999449616007303299,
#         999449808437792788,
#         999442532331175968,
#         999442625172099132,
#         999441568975048874,
#         999441660838674442
#     ]
    
#     diicot = [
#         999442143171072090,
#         999448152971169942,
#         999450505363333214,
#         999449634449653891,
#         999449765051908186,
#         999443232062722089,
#         999443241759944764,
#         999441768917512233,
#         999445368469201016
#     ]
#     smurd = [
#         999442153388376074,
#         999448727766970498,
#         999450517405171793,
#         999449241573396540,
#         999449785968885840,
#         999443269203271722,
#         999443278254575656,
#         999441826316566628,
#         999441833614651412
#     ]

#     politierol = [
#         999493803218046976,
#         999452220242272326,
#         999452219059478588,
#         999452217654382615,
#         999452332045648023,
#         999452380812820511,
#         999452220397465742,
#         999452211312590978,
#         999455078194876496,
#         999438314656510075
#     ]
    
#     diicotrol = [
#         999494667898994769,
#         999494701348573246,
#         999452218363215893,
#         999452214575775885,
#         999452332670603335,
#         999452217079775323,
#         999452216291229716,
#         999452219474710629,
#         999452221378932746,
#         999438481061326888
#     ]
    
#     smurdrol = [
#         999452330850267229,
#         999452331424878623,
#         999452334126010418,
#         999452599738712174,
#         999452602192371773,
#         999429537622396988
#     ]
    
    
#     politiegrade = [
    
#     ]
    
#     politiegrade = [
    
#     ]
    
    politiegrade = [
    999558907800322141,
    999564403403931698,
    999493801448054794
    ]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="rapoartepolitie")
    async def rapoartepd(self, ctx, idJoc, idDiscord):
          await ctx.send("T1")
          verif = False
            for x in permisiuni.politiegrade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        name = 'rapoarte-' + idJoc
                        await ctx.guild.create_text_channel(name, category=999720906303746168)
                        verif = True
                if verif == True:
                    break
            
#     @commands.command(name="rapoartediicot")
#     async def rapoartepd(self, ctx):
#           await ctx.guild.create_text_channel('', category=999720937295446067)
            
#     @commands.command(name="rapoartesmurd")
#     async def rapoartepd(self, ctx):
#           await ctx.guild.create_text_channel('', category=999720963849605190)
#         embed=discord.Embed(title="Metodă de verificare", description="Pentru a putea avea acces la restul server-ului, trebuie să reacționezi utilizând emoticonul <:imperial:999590871743868940>.", color=0xfff100)
#         embed.set_author(name="Imperial România", icon_url="https://media.discordapp.net/attachments/928411916857126973/928426116253892608/novnbdalsjkvsanbpov.png")
#         embed.set_image(url="https://cdn.discordapp.com/attachments/928411916857126973/928436594988449812/standard_4.gif")
#         embed.set_footer(text="All Right Reserved ©️ Imperial România")
#         await ctx.send(embed=embed)
#         manager = 999558907800322141
#         everyone = ctx.guild.get_role(999501365594292296) #ctx.guild.default_role
#         for x in permisiuni.politie:
#             c = self.bot.get_channel(x)
#             i = permisiuni.politie.index(x)
#             if i == 0 or i == 1 or i == 3 or i == 4:
#                 for y in permisiuni.politierol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i != 7 and i != 8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999564403403931698), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999493801448054794), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 for y in permisiuni.politierol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i==7 or i==8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999564403403931698), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999493801448054794), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(everyone, view_channel=True, manage_channels=False, manage_permissions=None, create_instant_invite=None, connect=None, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)

#         for x in permisiuni.diicot:
#             c = self.bot.get_channel(x)
#             i = permisiuni.diicot.index(x)
#             if i == 0 or i == 1 or i == 3 or i == 4:
#                 for y in permisiuni.diicotrol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i != 7 and i != 8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999494666355482636), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999494669492826162), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 for y in permisiuni.diicotrol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i==7 or i==8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999494666355482636), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999494669492826162), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(everyone, view_channel=True, manage_channels=False, manage_permissions=None, create_instant_invite=None, connect=None, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)

#         for x in permisiuni.smurd:
#             c = self.bot.get_channel(x)
#             i = permisiuni.smurd.index(x)
#             if i == 0 or i == 1 or i == 3 or i == 4:
#                 for y in permisiuni.smurdrol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i != 7 and i != 8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999495021462040636), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 await c.set_permissions(ctx.guild.get_role(999495026084163645), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#                 for y in permisiuni.smurdrol:
#                     await c.set_permissions(ctx.guild.get_role(y), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
#             elif i==7 or i==8:
#                 await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999495021462040636), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(ctx.guild.get_role(999495026084163645), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
#                 await c.set_permissions(everyone, view_channel=True, manage_channels=False, manage_permissions=None, create_instant_invite=None, connect=None, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
