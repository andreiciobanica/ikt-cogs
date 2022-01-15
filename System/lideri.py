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
        roluri_lider = [
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
            885152622842101790,
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
        roluri_colider = [
            ctx.guild.get_role(865215494813777960),
            ctx.guild.get_role(865215436748750849),
            ctx.guild.get_role(865215443546537995),
            ctx.guild.get_role(865215457161904168),
            ctx.guild.get_role(865215464363393104),
            ctx.guild.get_role(865215471640248321),
            ctx.guild.get_role(865215479358554123),
            ctx.guild.get_role(865215486693605377),
            ctx.guild.get_role(865215502014742559),
            ctx.guild.get_role(865215449708625932),
            865856937534029825,
            ctx.guild.get_role(903411093593001994),
            ctx.guild.get_role(892564801279123476),
            ctx.guild.get_role(908443445234901042),
            ctx.guild.get_role(918482448940171324),
            ctx.guild.get_role(920324980758155295),
            ctx.guild.get_role(929489167438708806),
            ctx.guild.get_role(929489144936271893),
            ctx.guild.get_role(929489155854061578),
            ctx.guild.get_role(865215429869961237)
            ]
        roluri_tester = [
            ctx.guild.get_role(865215493908463626),
            ctx.guild.get_role(865215435707252737),
            ctx.guild.get_role(865215442721570846),
            ctx.guild.get_role(865215456226967574),
            ctx.guild.get_role(865215463491239936),
            ctx.guild.get_role(865215470801780736),
            ctx.guild.get_role(865215478807789578),
            ctx.guild.get_role(865215486098014208),
            ctx.guild.get_role(865215501537378344),
            ctx.guild.get_role(865215449243582494),
            ctx.guild.get_role(885154848390127676),
            ctx.guild.get_role(903411278939316235),
            ctx.guild.get_role(892564804898803762),
            ctx.guild.get_role(908443563346501652),
            ctx.guild.get_role(918482393143345192),
            ctx.guild.get_role(920325133091078155),
            ctx.guild.get_role(929489166494998578),
            ctx.guild.get_role(929489137231343656),
            ctx.guild.get_role(929489156906836020),
            ctx.guild.get_role(865215429039226890)
            ]
        roluri_membru = [
            ctx.guild.get_role(865215492935385118),
            ctx.guild.get_role(865215434935762955),
            ctx.guild.get_role(865215441818222592),
            ctx.guild.get_role(865215455261491220),
            ctx.guild.get_role(865215462232293378),
            ctx.guild.get_role(865215469371654185),
            ctx.guild.get_role(865215477432320030),
            ctx.guild.get_role(865215484986392577),
            ctx.guild.get_role(865215500698648587),
            ctx.guild.get_role(865215448470650900),
            ctx.guild.get_role(885155574428360775),
            ctx.guild.get_role(903411660042174465),
            ctx.guild.get_role(892564807771897957),
            ctx.guild.get_role(908443944818454569),
            ctx.guild.get_role(918482112280141825),
            ctx.guild.get_role(920325233016205322),
            ctx.guild.get_role(929489165773570068),
            ctx.guild.get_role(929489128075173939),
            ctx.guild.get_role(929489157955391498),
            ctx.guild.get_role(865215428170219560)
            ]
        id_factiune = [
            ctx.guild.get_role(865215490782789632), # Araba
            ctx.guild.get_role(865215433174155344), # Triads
            ctx.guild.get_role(865215440182706196), # OTF
            ctx.guild.get_role(865215453235642410), # Siciliana
            ctx.guild.get_role(865215460815405056), # Ballas
            ctx.guild.get_role(865215467727224852), # Clanul Sportivilor
            ctx.guild.get_role(865215475835076678), # Groove Street
            ctx.guild.get_role(865215482767736833), # Bratva
            ctx.guild.get_role(865215498564534292), # Bloods
            ctx.guild.get_role(865215446848503808), # Arizona
            ctx.guild.get_role(885156306397315152), # Gomorra
            ctx.guild.get_role(903411840732790835), # Racoons
            ctx.guild.get_role(892564826671435847), # Los Vagos
            ctx.guild.get_role(908444404283490305), # Sons of Anarchy
            ctx.guild.get_role(918481525140488193), # Tokyo Manji
            ctx.guild.get_role(920325822852767744), # 6rats
            ctx.guild.get_role(929489164850831400), # Cosa Nostra
            ctx.guild.get_role(929489120433147905), # Crips
            ctx.guild.get_role(929489158584545372), # Loz Aztecas
            ctx.guild.get_role(931739070688817212) # Hitman
            ]
        for x in roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await ctx.message.author.send(x)
                    #await user.add_roles(roluri_colider[roluri_lider.index(x)])
            
    #@commands.command(name="tester", pass_context=True)
    #async def grade(self, ctx, user: discord.Member):
       # role = 440955056750198795
       # if any(item in roles for item in ctx.author.roles):
        #    await ctx.message.author.send(role) ---------- roluri_lider.index(x)
            
