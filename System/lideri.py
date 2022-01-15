# -*- coding: utf-8 -*-
from redbot.core import commands
from datetime import datetime, timedelta, timezone
from pytz import timezone
import discord

class lideri_grade(commands.Cog):
    roluri_lider = [
            865215495623934012, # Araba
            865215437531512842, # Triads
            865215444150648853, # OTF
            865215457672822815, # Siciliana
            865215465290334278, # Ballas
            865215472979279872, # Clanul Sportivilor
            865215480600199188, # Groove Street
            865215487864078357, # Bratva
            865215503320481812, # Bloods
            865215450883555338, # Arizona
            885152622842101790, # Gommora
            899760338436780042, # Racoons
            892118179269210152, # Los Vagos
            908442214047293450, # Sons of Anarchy
            918482495975084092, # Tokyo Manji
            920324660997001227, # 6rats
            929494693585227856, # Cosa Nostra
            929489148987981824, # Crips
            929489154079871008, # Loz Aztecas
            865215430662291496  # Hitman
            ]
    roluri_colider = [
            865215494813777960, # Araba
            865215436748750849, # Triads
            865215443546537995, # OTF
            865215457161904168, # Siciliana
            865215464363393104, # Ballas
            865215471640248321, # Clanul Sportivilor
            865215479358554123, # Groove Street
            865215486693605377, # Bratva
            865215502014742559, # Bloods
            865215449708625932, # Arizona
            865856937534029825, # Gommora
            903411093593001994, # Racoons
            892564801279123476, # Los Vagos
            908443445234901042, # Sons of Anarchy
            918482448940171324, # Tokyo Manji
            920324980758155295, # 6rats
            929489167438708806, # Cosa Nostra
            929489144936271893, # Crips
            929489155854061578, # Loz Aztecas
            865215429869961237  # Hitman
            ]
    roluri_tester = [
            865215493908463626, # Araba
            865215435707252737, # Triads
            865215442721570846, # OTF
            865215456226967574, # Siciliana
            865215463491239936, # Ballas
            865215470801780736, # Clanul Sportivilor
            865215478807789578, # Groove Street
            865215486098014208, # Bratva
            865215501537378344, # Bloods
            865215449243582494, # Arizona
            885154848390127676, # Gommora
            903411278939316235, # Racoons
            892564804898803762, # Los Vagos
            908443563346501652, # Sons of Anarchy
            918482393143345192, # Tokyo Manji
            920325133091078155, # 6rats
            929489166494998578, # Cosa Nostra
            929489137231343656, # Crips
            929489156906836020, # Loz Aztecas
            865215429039226890  # Hitman
            ]
    roluri_membru = [
            865215492935385118, # Araba
            865215434935762955, # Triads
            865215441818222592, # OTF
            865215455261491220, # Siciliana
            865215462232293378, # Ballas
            865215469371654185, # Clanul Sportivilor
            865215477432320030, # Groove Street
            865215484986392577, # Bratva
            865215500698648587, # Bloods
            865215448470650900, # Arizona
            885155574428360775, # Gommora
            903411660042174465, # Racoons
            892564807771897957, # Los Vagos
            908443944818454569, # Sons of Anarchy
            918482112280141825, # Tokyo Manji
            920325233016205322, # 6rats
            929489165773570068, # Cosa Nostra
            929489128075173939, # Crips
            929489157955391498, # Loz Aztecas
            865215428170219560  # Hitman
            ]
    id_factiune = [
            865215490782789632, # Araba
            865215433174155344, # Triads
            865215440182706196, # OTF
            865215453235642410, # Siciliana
            865215460815405056, # Ballas
            865215467727224852, # Clanul Sportivilor
            865215475835076678, # Groove Street
            865215482767736833, # Bratva
            865215498564534292, # Bloods
            865215446848503808, # Arizona
            885156306397315152, # Gomorra
            903411840732790835, # Racoons
            892564826671435847, # Los Vagos
            908444404283490305, # Sons of Anarchy
            918481525140488193, # Tokyo Manji
            920325822852767744, # 6rats
            929489164850831400, # Cosa Nostra
            929489120433147905, # Crips
            929489158584545372, # Loz Aztecas
            931739070688817212  # Hitman
            ]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        tz = timezone("Europe/Bucharest")

    @commands.command(name="colider", pass_context=True)
    async def colider(self, ctx, user: discord.Member):
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_colider[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de COLIDER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + user.id + ">!")
                    
    @commands.command(name="tester", pass_context=True)
    async def tester(self, ctx, user: discord.Member):
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_tester[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de TESTER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + user.id + ">!")
                    
    @commands.command(name="membru", pass_context=True)
    async def tester(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    verif = True
                    await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + user.id + ">!")
        if not verif:
            for x in lideri_grade.roluri_colider:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_colider.index(x)]))
                        await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]) +"> jucatorului <@" + user.id + ">!")
