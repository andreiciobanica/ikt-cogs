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
        932247900677865482,
        892118179269210152,
        899760338436780042,
        908442214047293450,
        918482495975084092,
        920324660997001227,
        929489148987981824,
        865215457672822815,
        865215472979279872,
        885152622842101790,
        935017101524082699,
        938207759403470889,
        962349255044005908
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
        932247374049456128,
        892564801279123476,
        903411093593001994,
        908443445234901042,
        918482448940171324,
        920324980758155295,
        929489144936271893,
        865215457161904168,
        865215471640248321,
        865856937534029825,
        935017585492234250,
        938207736691314708,
        962349669512532018
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
        932246795495563314,
        892564826671435847,
        903411840732790835,
        908444404283490305,
        918481525140488193,
        920325822852767744,
        929489120433147905,
        865215453235642410,
        865215467727224852,
        885156306397315152,
        935017996206870628,
        938206980789661697,
        962349602625957888
    ]

    regulament = [865215277922648094,
                909419605812998214,
                909418578128822302,
                909417928892502066,
                865215380893073428,
                909925632127934536,
                909418978982633482,
                908441807954784277,
                865215367314669568,
                893833971199275049,
                903409202700095528,
                908446168311287888,
                918484883976896523,
                920327017520582686,
                929862249735127161,
                930584842993795092,
                932315418264227861,
                934981038298501161,
                935729282825715713,
                938204817602519110,
                965604226497675304
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
                    935250323629551656,
                    932315483452096562,
                    934981090509193266,
                    935729313704189992,
                    938204862884233216,
                    965604240963817572
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
                935250343107907604,
                932315521439891506,
                934981134671052830,
                935729441718538331,
                938204942286598144,
                965604250627481628
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
        954741750218506340,
        905803399805681795,
        903409363107078214,
        908446788627857488,
        918485707327172628,
        920327715331145758,
        929862781518364743,
        935250363156680715,
        932315545729114142,
        934981318117322772,
        935729465663832114,
        954737105555308614,
        965604260999995392
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
        935250483990368376,
        932315656806862879,
        934981476334850148,
        935729652310364220,
        938205170398015548,
        965604273910075433
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
        935250628672905256,
        932315711563505694,
        934981522698665984,
        935729699290771506,
        938205220633182208,
        965604416533200976
        ]
    
    voce1 = [
        865215284709294110,
        885160178251599922,
        865215352237326337,
        865215324575629322,
        865215387042054185,
        865215343793143858,
        929901168451260447,
        865215364266459156,
        865215377285316609,
        893837187622264872,
        903409767869984849,
        908447015925604383,
        918486822726811658,
        920328724413567046,
        929892718837108737,
        935250790711443547,
        932315867239284756,
        934981618299445289,
        935729761349673031,
        938205326224805918,
        965604429564878908
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
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.regulament.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
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
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.imbracaminte.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
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
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=True, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.anunturi.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
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
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.chat.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
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
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.invoire.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=True, embed_links=True, attach_files=True, add_reactions=True, use_external_emojis=True, mention_everyone=True, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, manage_webhooks=False, create_instant_invite=None, send_messages=False, embed_links=None, attach_files=None, add_reactions=None, use_external_emojis=None, mention_everyone=None, manage_messages=False, read_message_history=True, send_tts_messages=False, use_slash_commands=None)

        for x in permisiuni.teste1:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.teste1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=True, manage_channels=None, manage_permissions=None, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)

        for x in permisiuni.voce1:
            c = self.bot.get_channel(x)
            #perms_manager = discord.Permissions(view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_lider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_colider = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_tester = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_membru = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_mafia = discord.Permissions(view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #perms_civil = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            #perms_muted = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
            #perms_everyone = discord.Permissions(view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(manager), view_channel=True, manage_channels=True, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.lideri[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.colideri[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.tester[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            #await c.set_permissions(ctx.guild.get_role(permisiuni.membru[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(permisiuni.mafia[permisiuni.voce1.index(x)]), view_channel=True, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=True, speak=True, priority_speaker=None, mute_members=True, deafen_members=True, move_members=True, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(civil), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
            await c.set_permissions(ctx.guild.get_role(muted), view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=False, priority_speaker=False, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=False)
            await c.set_permissions(everyone, view_channel=False, manage_channels=False, manage_permissions=False, create_instant_invite=None, connect=False, speak=True, priority_speaker=None, mute_members=False, deafen_members=False, move_members=False, use_voice_activation=None)
