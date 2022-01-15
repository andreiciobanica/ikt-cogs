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

OVERFLOW_ERROR = "The time set is way too high, consider setting something reasonable."

class lideri_grade(commands.Cog):
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
            865215430662291496, # Hitman
            865215533573341184, # Politie
            865215521094631435, # SIAS
            865215510265331712  # SMURD
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
            865215429869961237, # Hitman
            865215532654788648, # Politia Romana
            865215520445431838, # SIAS
            865215509178875934  # Sef de Statie
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
            865215429039226890, # Hitman
            865215528472805416, # Politia Romana
            865215516507504641, # SIAS
            885474291410407444  # SMURD
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
            931739070688817212, # Hitman
            865215523586048001, # Politia Romana
            865215512602345473, # SIAS
            931916048817586188  # SMURD
            ]

    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        global tz
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
    async def _add(self, ctx: commands.Context, user: discord.Member, *, time: TimeConverter):
        """
        Baga in somaj un jucator.
        Pentru durata, introduceti saptamani (w), zile (d), si/sau ore (h)[exemplu: 3h -> 3 ore; 2w -> 2 saptamani].
        """
        role = ctx.guild.get_role(893597206123274241)
        logs_channel_somaj = self.bot.get_channel(932033338347245628)
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
        await self._maybe_confirm(ctx, message)
        
        data_log = datetime.now(tz).strftime("%d %B %Y %H:%M:%S")
        embed=discord.Embed(title=f"{ctx.author.name} ({ctx.author.id}) - Adaugare Somaj", color=0x4b66ec)
        embed.add_field(name=f"{ctx.author} i-a dat somaj lui", value=f"{user.mention}", inline=False)
        embed.add_field(name="Durata", value=f"{time.days} zile si {time.seconds//3600} ore", inline=True)
        embed.set_footer(text=str(data_log))
        await logs_channel_somaj.send(embed=embed)
        #await self._maybe_send_log(ctx.guild, message)
        await self._tr_timer(user, role, end_time.timestamp())

    @commands.admin_or_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @_temp_role.command(name="elimina")
    async def _remove(self, ctx: commands.Context, user: discord.Member, role: discord.Role):
        """Scoate din somaj un jucator."""
        await self._tr_end(user, role, remover=ctx.author, ctx=ctx)
        await self._maybe_confirm(ctx, f"{role.mention} pentru {user.mention} a fost inlaturat.")

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
                        await member.remove_roles(role, reason=reason)
                        await self._maybe_send_log(
                            member.guild,
                            f"{role.mention} pentru {member.mention} a fost inlaturat."
                        )
                    else:
                        await self._maybe_send_log(
                            member.guild,
                            f"Perioada de {role.mention} pentru {member.mention} s-a incheiat, rolul v-a fost sters."
                        )
                else:
                    await self._maybe_send_log(
                        member.guild,
                        f"{role.mention} pentru {member.mention} nu a putut fi atribuit din cauza absentelor unor permisiuni."
                    )
            elif ctx:
                await ctx.send(f"Error: that is not an active TempRole.")

    @commands.command(name="colider", pass_context=True)
    async def colider(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_colider[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de COLIDER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
    
    @commands.command(name="tester", pass_context=True)
    async def tester(self, ctx, user: discord.Member):
        verif = False
        for x in lideri_grade.roluri_lider:
            for y in ctx.author.roles:
                if ctx.guild.get_role(x)==y:
                    await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_tester[lideri_grade.roluri_lider.index(x)]))
                    await ctx.send("Am atribuit rolul de TESTER <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                    verif = True
            if verif == True:
                break
                    
    @commands.command(name="membru", pass_context=True)
    async def membru(self, ctx, tip_factiune, user: discord.Member):
        verif = False
        if tip_factiune == "politie":
                for x in lideri_grade.politie_grade:
                    for y in ctx.author.roles:
                        if ctx.guild.get_role(x)==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[20]), ctx.guild.get_role(lideri_grade.roluri_politie[2]))
                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                            verif = True
                    if verif == True:
                        break
        elif tip_factiune == "sias":
                for x in lideri_grade.sias_grade:
                    for y in ctx.author.roles:
                        if ctx.guild.get_role(x)==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[21]), ctx.guild.get_role(lideri_grade.roluri_sias[3]))
                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[21]) +"> jucatorului <@" + str(user.id) + ">!")
                            verif = True
                    if verif == True:
                        break
        elif tip_factiune == "smurd":
                for x in lideri_grade.sias_grade:
                    for y in ctx.author.roles:
                        if ctx.guild.get_role(x)==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[22]), ctx.guild.get_role(lideri_grade.roluri_smurd[2]))
                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[22]) +"> jucatorului <@" + str(user.id) + ">!")
                            verif = True
                    if verif == True:
                        break
        elif tip_factiune == 'ilegala':
            if any(item in lideri_grade.roluri_lider[0:19] for item in ctx.author.roles) or any(item in lideri_grade.roluri_tester[0:19] for item in ctx.author.roles) or any(item in lideri_grade.roluri_colider[0:19] for item in ctx.author.roles):
                verif = False
                for x in lideri_grade.roluri_lider:
                    for y in ctx.author.roles:
                        if ctx.guild.get_role(x)==y:
                            verif = True
                            await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_lider.index(x)]), ctx.guild.get_role(865215401470066708))
                            await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_lider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                        if verif == True:
                            break
                if not verif:
                    for x in lideri_grade.roluri_colider:
                        for y in ctx.author.roles:
                            if ctx.guild.get_role(x)==y:
                                verif = True
                                await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_colider.index(x)]), ctx.guild.get_role(865215401470066708))
                                await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_colider.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                        if verif == True:
                            break
                if not verif:
                    for x in lideri_grade.roluri_tester:
                        for y in ctx.author.roles:
                            if ctx.guild.get_role(x)==y:
                                verif = True
                                await user.add_roles(ctx.guild.get_role(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(lideri_grade.roluri_membru[lideri_grade.roluri_tester.index(x)]), ctx.guild.get_role(865215401470066708))
                                await ctx.send("Am atribuit rolul de MEMBRU <@&" + str(lideri_grade.id_factiune[lideri_grade.roluri_tester.index(x)]) +"> jucatorului <@" + str(user.id) + ">!")
                        if verif == True:
                            break
    
    @commands.command(name="comisarsef", pass_context=True)
    async def comisarsef(self, ctx, user: discord.Member):
            verif = False
            for y in ctx.author.roles:
                if ctx.guild.get_role(lideri_grade.politie_grade[0])==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[2]))
                            await ctx.send("Am atribuit rolul de Comisar Sef <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                            break
    
    @commands.command(name="comisar", pass_context=True)
    async def comisar(self, ctx, user: discord.Member):
            verif = False
            for y in ctx.author.roles:
                if ctx.guild.get_role(lideri_grade.politie_grade[0])==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[3]))
                            await ctx.send("Am atribuit rolul de Comisar <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                            break
   
    @commands.command(name="subcomisar", pass_context=True)
    async def subcomisar(self, ctx, user: discord.Member):
            verif = False
            for y in ctx.author.roles:
                if ctx.guild.get_role(lideri_grade.politie_grade[0])==y:
                            await user.add_roles(ctx.guild.get_role(lideri_grade.politie_grade[4]))
                            await ctx.send("Am atribuit rolul de Subcomisar <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                            break
    
    @commands.command(name="agentprincipal", pass_context=True)
    async def agentprincipal(self, ctx, tip_factiune, user: discord.Member):
        verif = False
        if tip_factiune == "politie":
            for x in lideri_grade.politie_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_politie[0]))
                        await ctx.send("Am atribuit rolul de Agent Principal <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        elif tip_factiune == "sias":
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[1]))
                        await ctx.send("Am atribuit rolul de Agent Special <@&" + str(lideri_grade.id_factiune[21]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                        
    @commands.command(name="agent", pass_context=True)
    async def agent(self, ctx, tip_factiune, user: discord.Member):
        verif = False
        if tip_factiune == "politie":
            for x in lideri_grade.politie_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_politie[1]))
                        await ctx.send("Am atribuit rolul de Agent <@&" + str(lideri_grade.id_factiune[20]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        elif tip_factiune == "sias":
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[2]))
                        await ctx.send("Am atribuit rolul de Agent <@&" + str(lideri_grade.id_factiune[21]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
    
    @commands.command(name="coordonator", pass_context=True)
    async def coordonatorsias(self, ctx, user: discord.Member):
            verif = False
            for x in lideri_grade.sias_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_sias[0]))
                        await ctx.send("Am atribuit rolul de Coordonator <@&" + str(lideri_grade.id_factiune[21]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break

    @commands.command(name="smurd", pass_context=True)
    async def smurd(self, ctx, pozitie, user: discord.Member):
        verif = False
        if pozitie == "medic":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[0]))
                        await ctx.send("Am atribuit rolul de Medic <@&" + str(lideri_grade.id_factiune[22]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        if pozitie == "paramedic":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[1]))
                        await ctx.send("Am atribuit rolul de Paramedic <@&" + str(lideri_grade.id_factiune[22]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
        if pozitie == "asistent":
            for x in lideri_grade.smurd_grade:
                for y in ctx.author.roles:
                    if ctx.guild.get_role(x)==y:
                        await user.add_roles(ctx.guild.get_role(lideri_grade.roluri_smurd[2]))
                        await ctx.send("Am atribuit rolul de Asistent <@&" + str(lideri_grade.id_factiune[22]) +"> jucatorului <@" + str(user.id) + ">!")
                        verif = True
                if verif == True:
                    break
                        
#    @commands.command(name="somaj", pass_context=True)
#    async def somaj(self, ctx, user: discord.Member, durata_zile: int):
#        verif = False
#        for x in lideri_grade.roluri_lider:
#            for y in ctx.author.roles:
#                if ctx.guild.get_role(x)==y:
#                    await user.add_roles(ctx.guild.get_role(893597206123274241))
#                    await ctx.send("L-am bagat in SOMAJ pe jucatorul <@" + str(user.id) + "> pentru **" + str(durata_zile) + " zile**" + "!")
#                    verif = True
#            if verif == True:
#                break
