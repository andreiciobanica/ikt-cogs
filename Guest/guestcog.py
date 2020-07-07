from redbot.core import commands
from tabulate import tabulate

class Guest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="getguests")
    async def getGuests(self, ctx):
        await ctx.send("```")
        for member in ctx.guild.members:
            for role in member.roles:
                if role.id == 462702735490285569:
                    s = "<@"+ str(member.id) +">"
                    await ctx.send(s)
        await ctx.send("```")