from redbot.core import commands
from tabulate import tabulate

class Guest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="getguests")
    async def getGuests(self, ctx):
        for member in ctx.guild.members:
            for role in member.roles: 
                if role.id == 462702735490285569:
                    await ctx.send("<@member.id>")