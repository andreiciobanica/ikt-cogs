# -*- coding: utf-8 -*-
import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

class permisiuni(commands.Cog):

    lideri = [
        865215487864078357,
        929494693585227856,
        865215503320481812,
        865215465290334278,
        865215437531512842,
        865215495623934012,
        865215450883555338,
        865215480600199188,
        865215444150648853,
        892118179269210152,
        899760338436780042,
        908442214047293450,
        918482495975084092,
        920324660997001227,
        929489148987981824,
        929489154079871008,
        865215457672822815,
        865215472979279872,
        885152622842101790
    ]

    colideri = [
        865215486693605377,
        929489167438708806,
        865215502014742559,
        865215464363393104,
        865215436748750849,
        865215494813777960,
        865215449708625932,
        865215479358554123,
        865215443546537995,
        892564801279123476,
        903411093593001994,
        908443445234901042,
        918482448940171324,
        920324980758155295,
        929489144936271893,
        929489155854061578,
        865215457161904168,
        865215471640248321,
        865856937534029825
    ]

    tester = [
        865215486098014208,
        929489166494998578,
        865215501537378344,
        865215463491239936,
        865215435707252737,
        865215493908463626,
        865215449243582494,
        865215478807789578,
        865215442721570846,
        892564804898803762,
        903411278939316235,
        908443563346501652,
        918482393143345192,
        920325133091078155,
        929489137231343656,
        929489156906836020,
        865215456226967574,
        865215470801780736,
        885154848390127676
    ]

    membru = [
        865215484986392577,
        929489165773570068,
        865215500698648587,
        865215462232293378,
        865215434935762955,
        865215492935385118,
        865215448470650900,
        865215477432320030,
        865215441818222592,
        892564807771897957,
        903411660042174465,
        908443944818454569,
        918482112280141825,
        920325233016205322,
        929489128075173939,
        929489157955391498,
        865215455261491220,
        865215469371654185,
        885155574428360775
    ]

    mafia = [
        865215482767736833,
        929489164850831400,
        865215498564534292,
        865215460815405056,
        865215433174155344,
        865215490782789632,
        865215446848503808,
        865215475835076678,
        865215440182706196,
        892564826671435847,
        903411840732790835,
        908444404283490305,
        918481525140488193,
        920325822852767744,
        929489120433147905,
        929489158584545372,
        865215453235642410,
        865215467727224852,
        885156306397315152
    ]

    regulament = [865215277922648094, #Bratva
                  909419605812998214, #Cosa
                  909418578128822302, #Bloods
                  909417928892502066, #Ballas
                  865215380893073428, #Triads
                  909925632127934536, #Araba
                  909418978982633482, #Arizona
                  908441807954784277, #Groove
                  865215367314669568, #OTF
                  893833971199275049, #Vagos
                  903409202700095528, #Racoons
                  908446168311287888, #Sons
                  918484883976896523, #Tokyo Manji
                  920327017520582686, #6Ratz
                  929862249735127161, #Crips
                  929900652702867476, #Aztecas
                  930584842993795092, #Siciliana
                  932315418264227861, #Clanul Sportivilor
                  934981038298501161 #Camorra
                  ]

    imbracaminte = [
                    865215283450740746,
                    909419850479308851,
                    865215351741612082,
                    909418247621861436,
                    865215385775243294,
                    909925751804018708,
                    909419185766010930,
                    865215362722037771,
                    865215376618291200,
                    893834177819082772,
                    903409471198478377,
                    908446763243962378,
                    918485897266221117,
                    920327838995980378,
                    929862393897553940,
                    929900702837399593,
                    935250323629551656,
                    932315483452096562,
                    934981090509193266
                  ]

    anunturi = [
                865215280455221268,
                909419680983318578,
                909418645413822496,
                909418140478373918,
                865215382893887488,
                909925699496865842,
                909419057361604648,
                908441936669573170,
                914780628359217192,
                893834063511699456,
                903409300146368573,
                908446735687376966,
                918485384181198859,
                920327364628606976,
                929893684193943602,
                929900784320131152,
                935250343107907604,
                932315521439891506,
                934981134671052830
                  ]

    chat = [
        896820928263127141,
        909419747198783578,
        909418673905733672,
        909418174297038848,
        865215383866966016,
        909925717331038248,
        909419325453107260,
        865215360819265546,
        865215370347413555,
        905803399805681795,
        903409363107078214,
        908446788627857488,
        918485707327172628,
        920327715331145758,
        929862781518364743,
        929900857582047273,
        935250363156680715,
        932315545729114142,
        934981318117322772
        ]

    taxe = [
        881962763201691688,
        909419917655310376,
        909418837781385266,
        881963502749777990,
        881966919782105118,
        909925804576755792,
        881965407785873469,
        881966009928519760,
        881966721844543488,
        893834261453496320,
        903409612735283260,
        908446883884716032,
        918486177256968242,
        920328098409480312,
        929864169551978606,
        929900902758907996,
        935250444400349265,
        932315624275857448,
        934981374337777684
        ]

    dovada = [
        881532990025506826,
        909419883425579009,
        909418782081040455,
        909418283315380294,
        881533366032302090,
        909925773404700763,
        909419378355888128,
        908800795502317608,
        881533326710669392,
        905803577375739944,
        903409548579176468,
        908446854763655229,
        918486295607648327,
        920328278391263232,
        929864591322787910,
        929900950703968317,
        932315639681523804,
        935250465527050311,
        934981420550590484
        ]

    invoire = [
        865215282393120808,
        909419798952292362,
        909418706956853329,
        909418209025855528,
        865215384886312960,
        909925734414418003,
        909419119017861140,
        865215361896939520,
        886392739804102718,
        905803518605139978,
        903409422351605771,
        908446819766399066,
        918486408027578368,
        920328385765466112,
        929864883711922296,
        929901008337895444,
        935250483990368376,
        932315656806862879,
        934981476334850148
        ]

    teste1 = [
        865733866797793321,
        885159905386979400,
        865708724935720960,
        865733789790502932,
        865710282540974101,
        865706102900391986,
        865733567489245205,
        865733518313914408,
        865712600327127061,
        903070667136720956,
        903409991896146010,
        908446949978550282,
        918486604237139998,
        920328495266148403,
        929892319711363072,
        929901046275407912,
        935250628672905256,
        932315711563505694,
        934981522698665984
        ]

    teste2 = [
        865733855150211073,
        885160030997991484,
        865708750413627422,
        865733764349296690,
        865710300865757184,
        865706130319081472,
        865733588690534410,
        865733534265638973,
        865712612988682250,
        903070619980156969,
        903409937286320148,
        908446983033856010,
        918486744972795904,
        920328527239335976,
        929892560485355601,
        929901128727019590,
        935250653079552010,
        932315729838112848,
        934981573009367140
        ]
    
    voce1 = [
        865215284709294110,
        885160178251599922,
        865215352237326337,
        865215324575629322,
        865215387042054185,
        865215343793143858,
        865215315444105287,
        865215364266459156,
        865215377285316609,
        893837187622264872,
        903409767869984849,
        908447015925604383,
        918486822726811658,
        920328724413567046,
        929892718837108737,
        929901168451260447,
        935250773636427776,
        932315867239284756,
        934981618299445289
        ]

    voce2 = [
        865215285635579924,
        885160180852084786,
        865215353733644318,
        865215325506764800,
        865215387960344576,
        865215344875536434,
        865215316760723476,
        865215365386993695,
        865215378761973790,
        893837220946010142,
        903409835150811167,
        908447042093862962,
        918486930885332992,
        920328747637424168,
        929892850253066311,
        929901206405529700,
        935250790711443547,
        932315852970295347,
        934981661060378685
        ]


    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="permisiuni")
    async def permisiuni(self, ctx):
        manager = 865215567547727883
        civil = 907588821091221546
        muted = 892836101117587456
        everyone = ctx.guild.default_role
        for x in permisiuni.regulament:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)


        for x in permisiuni.imbracaminte:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.anunturi:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), iew_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.chat:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.taxe:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.taxe.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.taxe.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.taxe.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.taxe.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.taxe.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
        
        for x in permisiuni.dovada:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.dovada.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.dovada.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.dovada.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.dovada.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.dovada.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.invoire:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.teste1:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)

        for x in permisiuni.teste2:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.teste2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.teste2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.teste2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.teste2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.teste2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)

        for x in permisiuni.voce1:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)

        for x in permisiuni.voce2:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.voce2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.voce2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.voce2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.voce2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.voce2.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, video=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, video=True, use_voice_activation=None)
