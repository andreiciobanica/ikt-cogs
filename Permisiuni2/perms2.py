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
        885488481487433758, # chat-choco
        943485936333897788  # kill-feed
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
    
    imperial = [
        930583333233123448, #campanie
        865215147681513512, #evenimente
        865215148751192064, #giveaway
        920369552964067358, #intrebari-frecv
        928402978036150352, #beneficii
        865215149694648361, #server-boost
        937562542652411964, #lista-staff
        937553013265039370  #feedback-staff
    ]
    
    evenimente = [
        941403921899995197 #show yourself
    ]

    shop = [
        865215157557526549, #ip-shop
        895639061140734002, #ip-case
    ]
    
    shop_donatii = [
        #910103886210138162, #donatii-neacordate
        920619711471960095  #licitatii
    ]
    
    civil = [
        865215169541570560, #free-chat
        865215171593109514, #meme
        904763186752921610, #sugestii
        904762382562250804, #sugestii-reg
        932007587711422474, #bot
        865215172720328744  #tiktok
    ]
    
    civili = [
            865215490782789632, # Araba
            865215433174155344, # Cartof
            932246795495563314, # Albanian
            865215453235642410, # Siciliana
            865215460815405056, # Ballas
            865215467727224852, # Clanul Sportivilor
            865215475835076678, # Groove Street
            865215482767736833, # Bratva
            865215498564534292, # Yakuza
            865215446848503808, # Arizona
            885156306397315152, # Camorra
            903411840732790835, # Racoons
            892564826671435847, # Los Vagos
            908444404283490305, # Sons of Anarchy
            918481525140488193, # Tokyo Manji
            920325822852767744, # 6rats
            929489164850831400, # Cosa Nostra
            929489120433147905, # Crips
            929489158584545372, # Loz Aztecas
            931739070688817212, # Hitman
            935017996206870628, # Omerta
            938206980789661697, #Marabunta Grande
            936411187422330950, # Taxi
            914407701260431361, # Mecanic
            865215523586048001, # Politia Romana
            865215512602345473, # SIAS
            931916048817586188  # SMURD
    ]
    
    extra = [865215535947710466, 865215542734356490, 886270681325649970, 865215552485851167, 923175781637697606, 929489162850152469, 941217820363096146, 941413701456646204, 865243528476753921, 893597206123274241, 907952459505352714, 865215414018768926, 865215413179908107, 907877902043975711, 865215410471305226, 865215409716592660, 907952924355887104, 865215409716592660, 907952924355887104, 865215417391251456, 865215416456445952, 907953214731730964, 865215420889825311, 865215420025929729, 916334742314569778, 955074419309559819, 954862013362872340]
    donatori = [865215543634821160, 865215538791972895, 865215585838432286, 865215583963709460, 875537273666539520, 865215426182774804, 865215424952795147, 865215424094404640, 865215423392514048, 866634644602355773]
    resp = [865215550786633758, 865215551853035540]
    atr = [865215567547727883, 865215566418411541, 941758011414831225]
    stf = [865215570843533332]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")
        
    @commands.command(name="toaterolurileIMP")
    async def toaterolurileIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.civili:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959691074966781962))
                    
    @commands.command(name="extraIMP")
    async def extraIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.extra:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959689948519338064))
                    
    @commands.command(name="donatIMP")
    async def donatIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.donatori:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959698678950531072))
                    
    @commands.command(name="respIMP")
    async def respIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.resp:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959689661041745951))
                    
    @commands.command(name="atrIMP")
    async def atrIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.atr:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959698491746189345))
                    
    @commands.command(name="stfIMP")
    async def stfIMP(self, ctx):
        for x in ctx.guild.members:
            for y in permisiuni_imperial.stf:
                if ctx.guild.get_role(y) in x.roles:
                    await x.add_roles(ctx.guild.get_role(959689081640587274))

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
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
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

        for x in permisiuni_imperial.imperial:
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

        for x in permisiuni_imperial.shop:
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
            
        for x in permisiuni_imperial.shop_donatii:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 10):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            for i in range(10, 20):
                 await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni_imperial.evenimente:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 10):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            for i in range(10, 20):
                 await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni_imperial.civil:
            c = self.bot.get_channel(x)
            for j in range(20):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[j]), overwrite=None)
            for i in range(1, 10):
                await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            for i in range(10, 20):
                 await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[i]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni_imperial.roluri[0]), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=True, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=True, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
