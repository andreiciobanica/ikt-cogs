from redbot.core import commands

class Guest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="getguests")
    async def getGuests(self, ctx):
        await ctx.send("A")