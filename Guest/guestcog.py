from redbot.core import commands
from tabulate import tabulate

class Guest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="nouveniti")
    async def getguests(self, ctx):
        table = []
        for member in ctx.guild.members:
            for role in member.roles:
                if role.id == 462702735490285569:
                    s = "<@"+ str(member.id) +">"
                    table.append([s, member.name])
        await ctx.send("```"+tabulate(table, headers=["ID", "Nume"])+"```")