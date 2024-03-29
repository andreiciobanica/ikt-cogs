# -*- coding: utf-8 -*-
import typing
import asyncio
from datetime import datetime, timedelta, timezone
from pytz import timezone

import discord
from redbot.core import commands, Config
from redbot.core.utils.chat_formatting import humanize_list

if typing.TYPE_CHECKING:
    TimeConverter = timedelta
else:
    TimeConverter = commands.converter.TimedeltaConverter(
        minimum=timedelta(hours=1),
        allowed_units=["weeks", "days", "hours"],
        default_unit="days"
    )

OVERFLOW_ERROR = "Perioada de timp aleasa este prea mare. Cauta si tu ceva rezonabil!"

class lideri_grade(commands.Cog):
    high_staff_roles = [
            865215597247594517, # FULL ACCES
            865215596164284426, # Fondator Comunitate
            885846054547890197, # Developer
            865215595205492766, # Fondator
            877214428846772304, # Co-Fondator
            865215581162438677, # Supervizor
            865215580343631882, # Head of Staff
            865215598139801600, # Semi-Access
            865215577550094356, # Head of Moderators
            865215574392963082, # Head of Helpers
            865215587805954108, # Manager STAFF
            925389310423863396, # Super Admin
            865215578972880936  # Admin
    ]
    deep_web = [865215401470066708]
    politie_grade = [
            865215533573341184, # Lider Politie
            865215532654788648, # Chestor Sef
            900110938563313675, # Comisar Sef
            865215529807904809, # Comisar
            865215529039953923, # Sub Comisar
            865215528472805416  # Tester
    ]
    roluri_politie = [
            865215527639449620, # Agent Principal
            865215525608357958, # Agent
            865215524782866432  # Cadet
    ]
    roluri_rutiera = [
            908792926207881276, # Lider Rutiera
            908793125475082250  # Rutiera
    ]
    sias_grade = [
            865215521094631435, # General SIAS
            865215520445431838, # Co-General SIAS
            865215519523209246, # Procuror SIAS
            865215518650531870, # Sub Procuror SIAS
            865215516507504641  # Tester
    ]
    roluri_sias = [
            865215515210416179, # Coordonator SIAS
            865215514624131072, # Agent Special SIAS
            865215513800867850, # Agent SIAS
            931961302342058104  # Recrut SIAS
    ]
    smurd_grade = [
            865215510265331712, # Director SMURD
            865215509178875934, # Sef de Statie
            885474291410407444  # Tester SMURD
    ]
    roluri_smurd = [
            865215507989004328, # Medic
            865215507183566908, # Paramedic
            865215506239324180  # Asistent
    ]
    faction_restriction = [
            865215523080241192, # Politia Romana
            865215512098242570, # SIAS
            865215505023238155, # Medic
            885162367149809664  # Hitman
    ]
    roluri_lider = [
            865215495623934012, # Araba
            865215437531512842, # Cartof
            932247900677865482, # OTF
            865215457672822815, # Siciliana
            865215465290334278, # Ballas
            865215472979279872, # Clanul Sportivilor
            865215480600199188, # Groove Street
            865215487864078357, # Bratva
            865215503320481812, # Bloods
            865215450883555338, # Arizona
            885152622842101790, # Camorra
            899760338436780042, # Racoons
            892118179269210152, # Los Vagos
            908442214047293450, # Sons of Anarchy
            918482495975084092, # Tokyo Manji
            920324660997001227, # 6rats
            929494693585227856, # Cosa Nostra
            929489148987981824, # Crips
            929489154079871008, # Loz Aztecas
            865215430662291496, # Hitman
            935017101524082699, # Omerta
            938207759403470889, # Marabunta Grande
            962349255044005908, # Corleone
            914406930880024576, # Taxi
            914407704125116478, # Mecanic
            865215533573341184, # Politie
            865215521094631435, # SIAS
            865215510265331712  # SMURD
            ]
    roluri_colider = [
            865215494813777960, # Araba
            865215436748750849, # Cartof
            932247374049456128, # Albanian
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
            865215429869961237, # Hitman
            935017585492234250, # Omerta
            938207736691314708, # Marabunta Grande
            962349669512532018, # Corleone
            936411187422330950, # Taxi
            914407701260431361, # Mecanic
            865215532654788648, # Politia Romana
            865215520445431838, # SIAS
            865215509178875934  # Sef de Statie
            ]
    id_factiune = [
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
            938206980789661697, # Marabunta Grande
            962349602625957888, # Corleone
            936411187422330950, # Taxi
            914407701260431361, # Mecanic
            865215523586048001, # Politia Romana
            865215512602345473, # SIAS
            931916048817586188  # SMURD
            ]
    
    rol_factiune = [959691074966781962]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
        global logs_channel_somaj
        global logs_channel_factionrestriction
        global logs_channel_gradefactiune
        logs_channel_somaj = self.bot.get_channel(932033338347245628)
        logs_channel_factionrestriction = self.bot.get_channel(932333705802973184)
        logs_channel_gradefactiune = self.bot.get_channel(932066407909322812)
        tz = timezone("Europe/Bucharest")
        self.config = Config.get_conf(self, identifier=14000605, force_registration=True)
        default_guild = {
            "log": None,
            "confirmation": True,
            "allowed": []
        }
        default_member = {
            "temp_roles": {}
        }
        self.config.register_guild(**default_guild)
        self.config.register_member(**default_member)
        
        self.tr_handler_task = self.bot.loop.create_task(self._tr_handler())
        
        
    def cog_unload(self):
        self.tr_handler_task.cancel()

    @commands.guild_only()
    @commands.group(name="somaj")
    async def _temp_role(self, ctx: commands.Context):
        """Comenzi SOMAJ"""

    @commands.bot_has_permissions(manage_roles=True)
    @_temp_role.command(name="adauga")
    async def _add(self, ctx: commands.Context, user: discord.Member, time: TimeConverter):
        """
        Baga in somaj un jucator.
        Pentru durata, introduceti saptamani (w), zile (d), si/sau ore (h)[exemplu: 3h -> 3 ore; 2w -> 2 saptamani].
        """
        verif = False
        for x in ctx.author.roles:
            for y in lideri_grade.roluri_lider:
                if ctx.guild.get_role(y) == x:
                    role = ctx.guild.get_role(893597206123274241)
                    if role in user.roles:
                        return await ctx.send(f"Acest jucator este deja in {role.mention}!")

                    if role >= ctx.guild.me.top_role or (role >= ctx.author.top_role and ctx.author != ctx.guild.owner):
                        return await ctx.send("That role cannot be assigned due to the Discord role hierarchy!")

                    async with self.config.member(user).temp_roles() as user_tr:
                        if user_tr.get(str(role.id)):
                            return await ctx.send(
                                f"{user.mention} se afla in somaj!",
                                allowed_mentions=discord.AllowedMentions.none()
                            )
                        try:
                            end_time = datetime.now() + time
                        except OverflowError:
                            return await ctx.send(OVERFLOW_ERROR)
                        user_tr[str(role.id)] = end_time.timestamp()

                    if role < ctx.guild.me.top_role:
                        if role not in user.roles:
                            await user.add_roles(
                                role,
                                reason=f"Somaj: adaugat de catre {ctx.author}, expira in {time.days} zile {time.seconds//3600} ore"
                            )
                    else:
                        return await ctx.send("Nu pot sa atribui acest rol!")

                    message = f"{role.mention} a fost atribuit lui {user.mention}. Expira in {time.days} zile {time.seconds//3600} ore."
                    verif = True
                    await self._maybe_confirm(ctx, message)

                    reason = "A primit somer."
                    for x in user.roles:
                        if (x.id in lideri_grade.roluri_colider) or (x.id in lideri_grade.id_factiune) or (x.id in lideri_grade.roluri_smurd) or (x.id in lideri_grade.smurd_grade) or (x.id in lideri_grade.roluri_sias) or (x.id in lideri_grade.sias_grade) or (x.id in lideri_grade.roluri_rutiera) or (x.id in lideri_grade.roluri_politie) or (x.id in lideri_grade.politie_grade) or (x.id in lideri_grade.deep_web) or (x.id in lideri_grade.rol_factiune):
                            #await ctx.send(str(x) + ": " + str(x.id))
                            await user.remove_roles(x, reason=reason)

                    data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                    embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Adaugare Somaj", color=0x4b66ec)
                    embed.add_field(name=f"{ctx.author} i-a dat somaj lui", value=f"{user.mention}", inline=False)
                    embed.add_field(name="Durata", value=f"{time.days} zile si {time.seconds//3600} ore", inline=True)
                    embed.set_footer(text=str(data_log))
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    await self.bot.get_channel(932033338347245628).send(embed=embed)
                    await self._tr_timer(user, role, end_time.timestamp())
                    #await self._maybe_send_log(ctx.guild, message)
                if verif == True:
                    break
        if verif == False:
            await self._maybe_confirm(ctx, f"Doar un lider poate sa bage in somaj un jucator!")

    @commands.admin_or_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @_temp_role.command(name="inlatura")
    async def _remove(self, ctx: commands.Context, user: discord.Member):
        """Scoate din somaj un jucator."""
        verif = False
        for x in ctx.author.roles:
            for y in lideri_grade.high_staff_roles:
                if ctx.guild.get_role(y) == x:
                    role = ctx.guild.get_role(893597206123274241)
                    await self._tr_end(user, role, remover=ctx.author, ctx=ctx)
                    await self._maybe_confirm(ctx, f"{role.mention} pentru {user.mention} a fost inlaturat.")
                    verif = True
            if verif == True:
                break
        if verif == False:
            await self._maybe_confirm(ctx, f"Doar un membru din High Staff poate sa inlature somajul unui jucator!")
                    

    @_temp_role.command(name="ramas")
    async def _remaining(self, ctx: commands.Context):
        """Verifica cat timp mai ai somaj."""
        role = ctx.guild.get_role(893597206123274241)
        user = ctx.author
        async with self.config.member(user).temp_roles() as user_tr:
            if not (cur_tr := user_tr.get(str(role.id))):
                return await ctx.send(
                    f"That is not an active TempRole for {user.mention}.",
                    allowed_mentions=discord.AllowedMentions.none()
                )
            r_time = datetime.fromtimestamp(cur_tr) - datetime.now()
            return await ctx.maybe_send_embed(f"**Timp ramas:** {r_time.days} zile {round(r_time.seconds/3600, 1)} ore")

    @commands.bot_has_permissions(embed_links=True)
    @_temp_role.command(name="lista")
    async def _list(self, ctx: commands.Context, user: discord.Member = None):
        """Afiseaza toti somerii."""
        desc = ""
        if not user:
            title = f"{ctx.guild.name} - Lista Somaj"
            for member_id, temp_roles in (await self.config.all_members(ctx.guild)).items():
                member: discord.Member = ctx.guild.get_member(int(member_id))
                if member:
                    if roles := [ctx.guild.get_role(int(r)) for r in temp_roles["temp_roles"].keys()]:
                        desc += f"{member.mention}: {humanize_list([r.mention for r in roles])}:\n"
                    else:
                        await self.config.member(member).clear()
        else:
            title = f"{user.display_name} - Durata somaj"
            async with self.config.member(user).temp_roles() as member_temp_roles:
                for temp_role, end_ts in member_temp_roles.items():
                    role: discord.Role = ctx.guild.get_role(int(temp_role))
                    if role:
                        r_time = datetime.fromtimestamp(end_ts) - datetime.now()
                        desc += f"{role.mention}: ends in {r_time.days}d {round(r_time.seconds/3600, 1)}h\n"
                    else:
                        del member_temp_roles[temp_role]
        return await ctx.send(embed=discord.Embed(
            title=title,
            description=desc,
            color=await ctx.embed_color()
        ))

    @commands.admin_or_permissions(manage_roles=True)
    @_temp_role.command(name="logchannel")
    async def _log_channel(self, ctx: commands.Context, channel: discord.TextChannel = None):
        """Set the TempRole log channel for the server (leave blank to remove)."""
        if channel and not channel.permissions_for(ctx.guild.me).send_messages:
            return await ctx.send(f"I cannot send messages to {channel.mention}!")
        await self.config.guild(ctx.guild).log.set(channel.id if channel else None)
        return await ctx.tick()

    @commands.admin_or_permissions(manage_roles=True)
    @_temp_role.command(name="mesajconfirmare")
    async def _confirmation(self, ctx: commands.Context, true_or_false: bool):
        """Toggle whether to send confirmation messages after TempRole commands."""
        await self.config.guild(ctx.guild).confirmation.set(true_or_false)
        return await ctx.tick()

    async def _maybe_confirm(self, ctx: commands.Context, message: str):
        if await self.config.guild(ctx.guild).confirmation():
            await ctx.send(message, allowed_mentions=discord.AllowedMentions.none())

    async def _maybe_send_log(self, guild: discord.Guild, message: str):
        log_channel = await self.config.guild(guild).log()
        if log_channel and (log_channel := guild.get_channel(log_channel)) and log_channel.permissions_for(guild.me).send_messages:
            await log_channel.send(
                message,
                allowed_mentions=discord.AllowedMentions.none()
            )

    async def _tr_handler(self):
        await self.bot.wait_until_red_ready()
        try:
            tr_coros = []
            for guild_id, members in (await self.config.all_members()).items():
                guild: discord.Guild = self.bot.get_guild(int(guild_id))
                for member_id, temp_roles in members.items():
                    member: discord.Member = guild.get_member(int(member_id))
                    for tr, ts in temp_roles["temp_roles"].items():
                        role: discord.Role = guild.get_role(int(tr))
                        tr_coros.append(self._tr_timer(member, role, ts))
            await asyncio.gather(*tr_coros)
        except Exception:
            pass

    async def _tr_timer(self, member: discord.Member, role: discord.Role, end_timestamp: float):
        seconds_left = (datetime.fromtimestamp(end_timestamp) - datetime.now()).total_seconds()
        if seconds_left > 0:
            await asyncio.sleep(seconds_left)
        await self._tr_end(member, role)

    async def _tr_end(self, member: discord.Member, role: discord.Role, remover=None, ctx=None):
        async with self.config.member(member).temp_roles() as tr_entries:
            if tr_entries.get(str(role.id)):
                del tr_entries[str(role.id)]
                reason = "Somer: timpul s-a scurs" if not remover else f"Somer: scos de catre {remover}"
                if member.guild.me.guild_permissions.manage_roles and role < member.guild.me.top_role:
                    if role in member.roles:
                        if remover == None:
                            await member.remove_roles(role, reason=reason)
                            data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                            embed=discord.Embed(title=f"{member} ({member.id}) - Expirare Somaj", color=0xf1c232)
                            embed.add_field(name=f"A expirat perioada de somaj lui", value=f"{member.mention}", inline=False)
                            embed.set_footer(text=str(data_log))
                            embed.set_thumbnail(url=member.avatar_url)
                            await self.bot.get_channel(932033338347245628).send(embed=embed)
                        else:
                            await member.remove_roles(role, reason=reason)
                            data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                            embed=discord.Embed(title=f"{remover} ({remover.id}) - Inlaturare Somaj", color=0xec4b4b)
                            embed.add_field(name=f"{remover} i-a scos somajul lui", value=f"{member.mention}", inline=False)
                            embed.set_footer(text=str(data_log))
                            embed.set_thumbnail(url=remover.avatar_url)
                            await self.bot.get_channel(932033338347245628).send(embed=embed)
                        #await self._maybe_send_log(
                        #    member.guild,
                        #    f"{role.mention} pentru {member.mention} a fost inlaturat."
                        #)
                    else:                
                        #data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                        #embed=discord.Embed(title=f"{remover} ({remover.id}) - Inlaturare Somaj", color=0x4b66ec)
                        #embed.add_field(name=f"{remover} i-a scos somajul lui", value=f"{member.mention}", inline=False)
                        #embed.set_footer(text=str(data_log))
                        #await self.self.bot.get_channel(932033338347245628).send(embed=embed)
                        await self._maybe_send_log(
                            member.guild,
                            f"Perioada de {role.mention} pentru {member.mention} s-a incheiat, rolul v-a fost sters."
                        )
                else:
                    await self._maybe_send_log(
                        member.guild,
                        f"{role.mention} pentru {member.mention} nu a putut fi scos din cauza absentelor unor permisiuni."
                    )
            elif ctx:
                await ctx.send(f"Error: that is not an active TempRole.")

    
    @commands.group(name="colider")
    async def colider(self, ctx: commands.Context):
        """Adauga sau inlatura un colider factiunii tale(**Doar pentru LIDERI**)"""

    @commands.bot_has_permissions(manage_roles=True)
    @colider.command(name="adauga")
    async def _adaugacolider(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_colider[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de COLIDER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                
    @commands.bot_has_permissions(manage_roles=True)
    @colider.command(name="inlatura", pass_context=True)
    async def _inlaturacolider(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_colider[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am inlaturat rolul de COLIDER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
    
#    @commands.group(name="tester")
#    async def tester(self, ctx: commands.Context):
#        """Adauga sau inlatura un tester factiunii tale(**Doar pentru LIDERI**)"""

#    @commands.bot_has_permissions(manage_roles=True)
#    @tester.command(name="adauga", pass_context=True)
#    async def _adaugatester(self, ctx, user: discord.Member):
#        verif = False
#        for x in lideri_grade.roluri_lider:
#            for y in ctx.author.roles:
#                if ctx.guild.get_role(x)==y:
#                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_tester[lideri_grade.roluri_lider.index(x)]))
#                    await ctx.send("Am atribuit rolul de TESTER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
#                    verif = True
#            if verif == True:
#                break
                
#    @commands.bot_has_permissions(manage_roles=True)
#    @tester.command(name="inlatura", pass_context=True)
#    async def _inlaturatester(self, ctx, user: discord.Member):
#        verif = False
#        for x in lideri_grade.roluri_lider:
#            for y in ctx.author.roles:
#                if ctx.guild.get_role(x)==y:
#                    await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_tester[lideri_grade.roluri_lider.index(x)]))
#                    await ctx.send("Am inlaturat rolul de TESTER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
#                    verif = True
#            if verif == True:
#                break
    
    @commands.group(name="membru")
    async def membru(self, ctx: commands.Context):
        """Adauga sau inlatura un membru din factiunea dvs."""
        
    @membru.command(name="adauga", pass_context=True)
    async def _adaugamembru(self, ctx, user: discord.Member):
        veriff = False
        for x in lideri_grade.politie_grade:
            if ctx.guild.get_role(x) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[25]), ctx.guild.get_role(lideri_grade.roluri_politie[2]), ctx.guild.get_role(959691074966781962))
                await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                veriff = True
            if veriff:
                break
        
        if not veriff:
            for x in lideri_grade.sias_grade:
                if ctx.guild.get_role(x) in ctx.author.roles:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[26]), ctx.guild.get_role(lideri_grade.roluri_sias[3]), ctx.guild.get_role(959691074966781962))
                    await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                    veriff = True
                if veriff:
                    break
        
        if not veriff:
            for x in lideri_grade.smurd_grade:
                if ctx.guild.get_role(x) in ctx.author.roles:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[27]), ctx.guild.get_role(lideri_grade.roluri_smurd[2]), ctx.guild.get_role(959691074966781962))
                    await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[27]) +"> jucatorului <@" + str(user.id) + ">!")
                    veriff = True
                if veriff:
                    break
                    
        #if any(ctx.guild.get_role(item) in lideri_grade.roluri_lider[0:22] for item in ctx.author.roles) or any(ctx.guild.get_role(item) in lideri_grade.roluri_tester[0:22] for item in ctx.author.roles) or any(ctx.guild.get_role(item) in lideri_grade.roluri_colider[0:22] for item in ctx.author.roles):
        if not veriff:
            for x in lideri_grade.roluri_lider:
                if ctx.guild.get_role(x) in ctx.author.roles:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(865215401470066708), ctx.guild.get_role(959691074966781962))
                    await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    veriff = True
                if veriff:
                    break

        if not veriff:
            for x in lideri_grade.roluri_colider:
                if ctx.guild.get_role(x) in ctx.author.roles:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(865215401470066708), ctx.guild.get_role(959691074966781962))
                    await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    veriff = True
                if veriff:
                    break

        #if not verif:
        #    for x in lideri_grade.roluri_tester:
        #        if ctx.guild.get_role(x) in ctx.author.roles:
        #            verif = True
        #            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(865215401470066708))
        #            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
        #        if verif == True:
        #            break
    
    @membru.command(name="inlatura", pass_context=True)
    async def _inlaturamembru(self, ctx, user: discord.Member):
        verif = False
        for y in lideri_grade.roluri_lider:
            if ctx.guild.get_role(y) in ctx.author.roles:
                reason = f"{user.mention} a fost inlaturat de catre liderul {ctx.author}."
                verif = True
                for x in user.roles:
                    if (x.id in lideri_grade.roluri_colider) or (x.id in lideri_grade.id_factiune) or (x.id in lideri_grade.roluri_smurd) or (x.id in lideri_grade.smurd_grade[1:]) or (x.id in lideri_grade.roluri_sias) or (x.id in lideri_grade.sias_grade[1:]) or (x.id in lideri_grade.roluri_rutiera) or (x.id in lideri_grade.roluri_politie) or (x.id in lideri_grade.politie_grade[1:]) or (x.id in lideri_grade.deep_web) or (x.id in lideri_grade.rol_factiune):
                        await user.remove_roles(x, reason=reason)
        if not verif:
            for y in lideri_grade.roluri_colider:
                if ctx.guild.get_role(y) in ctx.author.roles:
                    reason = f"{user.mention} a fost inlaturat de catre coliderul {ctx.author}."
                    verif = True
                    for x in user.roles:
                        if (x.id in lideri_grade.id_factiune) or (x.id in lideri_grade.smurd_grade) or (x.id in lideri_grade.sias_grade) or (x.id in lideri_grade.politie_grade) or (x.id in lideri_grade.deep_web) or (x.id in lideri_grade.rol_factiune):
                            await user.remove_roles(x, reason=reason)
        #if verif == False:
        #    for y in lideri_grade.roluri_tester:
        #        if ctx.guild.get_role(y) in ctx.author.roles:
        #            reason = f"{user.mention} a fost inlaturat de catre tester-ul {ctx.author}."
        #            verif = True
        #            for x in user.roles:
        #                if  (x.id in lideri_grade.roluri_membru) or (x.id in lideri_grade.id_factiune) or (x.id in lideri_grade.smurd_grade) or (x.id in lideri_grade.sias_grade) or (x.id in lideri_grade.politie_grade) or (x.id in lideri_grade.deep_web):
        #                    await user.remove_roles(x, reason=reason)
        
    #@commands.command(name="membru", pass_context=True)
    #async def membru(self, ctx, tip_factiune, user: discord.Member):
    #    verif = False
    #    if tip_factiune == "politie":
    #            for x in lideri_grade.politie_grade:
    #                for y in ctx.author.roles:
    #                   if ctx.guild.get_role(x)==y:
    #                      await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[20]), ctx.guild.get_role(lideri_grade.roluri_politie[2]))
    #                        await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
    #                        verif = True
    #                if verif == True:
    #                    break
    #    elif tip_factiune == "sias":
    #            for x in lideri_grade.sias_grade:
    #                for y in ctx.author.roles:
    #                    if ctx.guild.get_role(x)==y:
    #                        await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[21]), ctx.guild.get_role(lideri_grade.roluri_sias[3]))
    #                        await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[21]) +"> jucatorului <@" + str(user.id) + ">!")
    #                        verif = True
    #                if verif == True:
    #                    break
    #    elif tip_factiune == "smurd":
    #            for x in lideri_grade.smurd_grade:
    #                for y in ctx.author.roles:
    #                    if ctx.guild.get_role(x)==y:
    #                        await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[22]), ctx.guild.get_role(lideri_grade.roluri_smurd[2]))
    #                        await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[22]) +"> jucatorului <@" + str(user.id) + ">!")
    #                        verif = True
    #                if verif == True:
    #                    break
    #    elif tip_factiune == 'ilegala':
    #        if any(item in lideri_grade.roluri_lider[0:19] for item in ctx.author.roles) or any(item in lideri_grade.roluri_tester[0:19] for item in ctx.author.roles) or any(item in lideri_grade.roluri_colider[0:19] for item in ctx.author.roles):
    #            verif = False
    #            for x in lideri_grade.roluri_lider:
    #                for y in ctx.author.roles:
    #                    if ctx.guild.get_role(x)==y:
    #                        verif = True
    #                        await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(865215401470066708))
    #                        await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
    #                    if verif == True:
    #                        break
    #            if not verif:
    #                for x in lideri_grade.roluri_colider:
    #                    for y in ctx.author.roles:
    #                        if ctx.guild.get_role(x)==y:
    #                            verif = True
    #                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(865215401470066708))
    #                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
    #                    if verif == True:
    #                        break
    #            if not verif:
    #                for x in lideri_grade.roluri_tester:
    #                    for y in ctx.author.roles:
    #                        if ctx.guild.get_role(x)==y:
    #                            verif = True
    #                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(865215401470066708))
    #                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
    #                   if verif == True:
    #                        break
                            
    # COMISAR SEF ---------------------------- INCEPUT
    @commands.group(name="comisarsef")
    async def comisarsef(self, ctx: commands.Context):
        """Adauga sau inlatura Comisar Sef(**Doar pentru LIDER**)"""

    @commands.bot_has_permissions(manage_roles=True)
    @comisarsef.command(name="adauga", pass_context=True)
    async def _adaugacomisarsef(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[2]))
                await ctx.send("Am atribuit rolul de Comisar Sef <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
            #break
            
                            
    @commands.bot_has_permissions(manage_roles=True)
    @comisarsef.command(name="inlatura", pass_context=True)
    async def _inlaturacomisarsef(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.politie_grade[2]))
                await ctx.send("Am inlaturat rolul de Comisar Sef <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                            #break
    # COMISAR SEF ---------------------------- SFARSIT    
    # COMISAR ---------------------------- INCEPUT
    @commands.group(name="comisar")
    async def comisar(self, ctx: commands.Context):
        """Adauga sau inlatura Comisar(**Doar pentru LIDER**)"""
    
    @commands.bot_has_permissions(manage_roles=True)   
    @comisar.command(name="adauga", pass_context=True)
    async def _adaugacomisar(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[3]))
                await ctx.send("Am atribuit rolul de Comisar <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
           #break
    @commands.bot_has_permissions(manage_roles=True)    
    @comisar.command(name="inlatura", pass_context=True)
    async def inlaturacomisar(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.politie_grade[3]))
                await ctx.send("Am inlaturat rolul de Comisar <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
            #break
    # COMISAR ---------------------------- SFARSIT        
    # SUBCOMISAR ---------------------------- INCEPUT
    @commands.group(name="subcomisar")
    async def subcomisar(self, ctx: commands.Context):
        """Adauga sau inlatura Subcomisar(**Doar pentru LIDER**)"""
    
    @commands.bot_has_permissions(manage_roles=True)
    @subcomisar.command(name="adauga", pass_context=True)
    async def adaugasubcomisar(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[4]))
                await ctx.send("Am atribuit rolul de Subcomisar <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
            #break
            
    @commands.bot_has_permissions(manage_roles=True)
    @subcomisar.command(name="inlatura", pass_context=True)
    async def inlaturasubcomisar(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.politie_grade[4]))
                await ctx.send("Am inlaturat rolul de Subcomisar <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
            #break
    # SUBCOMISAR ---------------------------- SFARSIT
    # AGENT PRINCIPAL ---------------------------- INCEPUT
    @commands.group(name="agentprincipal")
    async def agentprincipal(self, ctx: commands.Context):
        """Adauga sau inlatura Agent Principal/Special"""
        
    @agentprincipal.group(name="politie")
    async def agentprincipalpolitie(self, ctx: commands.Context):
        """Adauga sau inlatura Agent Principal din Politia Romana"""
        
    @agentprincipalpolitie.command(name="adauga", pass_context=True)
    async def adaugaagentprincipalpolitie(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.politie_grade:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_politie[0]))
                    await ctx.send("Am atribuit rolul de Agent Principal <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                    
    @agentprincipalpolitie.command(name="inlatura", pass_context=True)
    async def inlaturaagentprincipalpolitie(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.politie_grade:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_politie[0]))
                    await ctx.send("Am inlaturat rolul de Agent Principal <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                    
    @agentprincipal.group(name="sias")
    async def agentprincipalsias(self, ctx: commands.Context):
        """Adauga sau inlatura Agent Special din SIAS"""
        
    @agentprincipalsias.command(name="adauga", pass_context=True)
    async def adaugaagentprincipalsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[1]))
                        await ctx.send("Am atribuit rolul de Agent Special <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                    
    @agentprincipalsias.command(name="inlatura", pass_context=True)
    async def inlaturaagentprincipalsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_sias[1]))
                        await ctx.send("Am inlaturat rolul de Agent Special <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
    # AGENT PRINCIPAL ---------------------------- SFARSIT
    # AGENT ---------------------------- INCEPUT
    @commands.group(name="agent")
    async def agent(self, ctx: commands.Context):
        """Adauga sau inlatura Agent"""
    
    @agent.group(name="politie")
    async def agentpolitie(self, ctx: commands.Context):
        """Adauga sau inlatura Agent din Politia Romana"""
    
    @commands.bot_has_permissions(manage_roles=True)
    @agentpolitie.command(name="adauga", pass_context=True)
    async def adaugaagentpolitie(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.politie_grade:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_politie[1]))
                    await ctx.send("Am atribuit rolul de Agent <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                    
    @commands.bot_has_permissions(manage_roles=True)
    @agentpolitie.command(name="inlatura", pass_context=True)
    async def inlaturaagentpolitie(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.politie_grade:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_politie[1]))
                    await ctx.send("Am inlaturat rolul de Agent <@&" + str(lideri_grade.id_factiune[25]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                    
    @agent.group(name="sias")
    async def agentsias(self, ctx: commands.Context):
        """Adauga sau inlatura Agent din SIAS"""
        
    @commands.bot_has_permissions(manage_roles=True)
    @agentsias.command(name="adauga", pass_context=True)
    async def adaugaagentsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[2]))
                        await ctx.send("Am atribuit rolul de Agent <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                    
    @commands.bot_has_permissions(manage_roles=True)               
    @agentsias.command(name="inlatura", pass_context=True)
    async def inlaturaagentsias(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.sias_grade:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_sias[2]))
                    await ctx.send("Am inlaturat rolul de Agent <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
    # AGENT ---------------------------- SFARSIT
    # COORDONATOR SIAS ---------------------------- INCEPUT

    @commands.group(name="coordonator")
    async def coordonator(self, ctx: commands.Context):
        """Adauga sau inlatura Coordonator(**Doar pentru LIDER**)"""
    
    @commands.bot_has_permissions(manage_roles=True)
    @coordonator.command(name="adauga", pass_context=True)
    async def adaugacoordonatorsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[0]))
                        await ctx.send("Am atribuit rolul de Coordonator <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                    
    @commands.bot_has_permissions(manage_roles=True)
    @coordonator.command(name="inlatura", pass_context=True)
    async def inlaturacoordonatorsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.remove_roles(ctx.guild.get_role(lideri_grade.roluri_sias[0]))
                        await ctx.send("Am inlaturat rolul de Coordonator <@&" + str(lideri_grade.id_factiune[26]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
    # COORDONATOR SIAS ---------------------------- SFARSIT

    @commands.command(name="smurd", pass_context=True)
    async def smurd(self, ctx, pozitie, user: discord.Member):
        verif = False
        if pozitie == "medic":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[0]))
                        await ctx.send("Am atribuit rolul de Medic <@&" + str(lideri_grade.id_factiune[27]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        if pozitie == "paramedic":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[1]))
                        await ctx.send("Am atribuit rolul de Paramedic <@&" + str(lideri_grade.id_factiune[27]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        if pozitie == "asistent":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[2]))
                        await ctx.send("Am atribuit rolul de Asistent <@&" + str(lideri_grade.id_factiune[27]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                    
    # FACTION RESTRICTION
                        
    @commands.group(name="restriction")
    async def restriction(self, ctx: commands.Context):
        """Meniul Faction Restriction"""
    
    @restriction.group(name="politie", pass_context=True)
    async def restrictionpolitie(self, ctx: commands.Context):
        """Meniul Faction Restriction pentru Politia Romana"""

    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionpolitie.command(name="adauga", pass_context=True)
    async def adaugafactionrestrictionpolitie(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.faction_restriction[0]))
                await ctx.send("L-am adaugat pe jucatorul <@" + str(user.id) +"> pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[20]) + ">! (<@&" + str(lideri_grade.faction_restriction[0]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Atribuire Faction Restriction", color=0x4b66ec)
                embed.add_field(name=f"{ctx.author} i-a atribuit FACTION RESTRICTION lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[25]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
           #break
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionpolitie.command(name="inlatura", pass_context=True)
    async def inlaturafactionrestrictionpolitie(self, ctx, user: discord.Member):
            if ctx.guild.get_role(lideri_grade.politie_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.faction_restriction[0]))
                await ctx.send("L-am inlaturat pe jucatorul <@" + str(user.id) +"> de pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[20]) + ">! (<@&" + str(lideri_grade.faction_restriction[0]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Inlaturare Faction Restriction", color=0xec4b4b)
                embed.add_field(name=f"{ctx.author} i-a scos FACTION RESTRICTION-UL lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[25]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)

    @restriction.group(name="sias", pass_context=True)
    async def restrictionsias(self, ctx: commands.Context):
        """Meniul Faction Restriction pentru SIAS"""
        
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionsias.command(name="adauga", pass_context=True)
    async def adaugafactionrestrictionsias(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.sias_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.faction_restriction[1]))
                await ctx.send("L-am adaugat pe jucatorul <@" + str(user.id) +"> pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[21]) + ">! (<@&" + str(lideri_grade.faction_restriction[1]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Atribuire Faction Restriction", color=0x4b66ec)
                embed.add_field(name=f"{ctx.author} i-a atribuit FACTION RESTRICTION lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[26]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionsias.command(name="inlatura", pass_context=True)
    async def inlaturafactionrestrictionsias(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.sias_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.faction_restriction[1]))
                await ctx.send("L-am inlaturat pe jucatorul <@" + str(user.id) +"> de pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[21]) + ">! (<@&" + str(lideri_grade.faction_restriction[1]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Inlaturare Faction Restriction", color=0xec4b4b)
                embed.add_field(name=f"{ctx.author} i-a scos FACTION RESTRICTION-UL lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[26]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break

    @restriction.group(name="smurd", pass_context=True)
    async def restrictionsmurd(self, ctx: commands.Context):
        """Meniul Faction Restriction pentru SMURD"""

    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionsmurd.command(name="adauga", pass_context=True)
    async def adaugafactionrestrictionsmurd(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.smurd_grade[0]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.faction_restriction[2]))
                await ctx.send("L-am adaugat pe jucatorul <@" + str(user.id) +"> pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[22]) + ">! (<@&" + str(lideri_grade.faction_restriction[2]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Atribuire Faction Restriction", color=0x4b66ec)
                embed.add_field(name=f"{ctx.author} i-a atribuit FACTION RESTRICTION lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[27]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionsmurd.command(name="inlatura", pass_context=True)
    async def inlaturafactionrestrictionsmurd(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.smurd_grade[0]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.faction_restriction[2]))
                await ctx.send("L-am inlaturat pe jucatorul <@" + str(user.id) +"> de pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[22]) + ">! (<@&" + str(lideri_grade.faction_restriction[2]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Inlaturare Faction Restriction", color=0xec4b4b)
                embed.add_field(name=f"{ctx.author} i-a scos FACTION RESTRICTION-UL lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[27]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break

    @restriction.group(name="hitman", pass_context=True)
    async def restrictionhitman(self, ctx: commands.Context):
        """Meniul Faction Restriction pentru Hitman"""
        
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionhitman.command(name="adauga", pass_context=True)
    async def adaugafactionrestrictionhitman(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.roluri_lider[19]) in ctx.author.roles:
                await user.add_roles(ctx.guild.get_role(lideri_grade.faction_restriction[3]))
                await ctx.send("L-am adaugat pe jucatorul <@" + str(user.id) +"> pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[19]) + ">! (<@&" + str(lideri_grade.faction_restriction[3]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Atribuire Faction Restriction", color=0x4b66ec)
                embed.add_field(name=f"{ctx.author} i-a atribuit FACTION RESTRICTION lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[19]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break
    @commands.bot_has_permissions(manage_roles=True)   
    @restrictionhitman.command(name="inlatura", pass_context=True)
    async def inlaturafactionrestrictionhitman(self, ctx, user: discord.Member):
            #verif = False
            #for y in ctx.author.roles:
            if ctx.guild.get_role(lideri_grade.roluri_lider[19]) in ctx.author.roles:
                await user.remove_roles(ctx.guild.get_role(lideri_grade.faction_restriction[3]))
                await ctx.send("L-am inlaturat pe jucatorul <@" + str(user.id) +"> de pe lista de persoane non-grata pentru <@&" + str(lideri_grade.id_factiune[19]) + ">! (<@&" + str(lideri_grade.faction_restriction[3]) + ">)")
                data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
                embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Inlaturare Faction Restriction", color=0xec4b4b)
                embed.add_field(name=f"{ctx.author} i-a scos FACTION RESTRICTION-UL lui", value=f"{user.mention}", inline=False)
                embed.add_field(name="Factiune", value=f"{lideri_grade.id_factiune[19]}", inline=True)
                embed.set_footer(text=str(data_log))
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await self.bot.get_channel(932333705802973184).send(embed=embed)
            #break
    # END FACTION RESTRICTION
