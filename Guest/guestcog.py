from redbot.core import commands

class Guest(commands.Cog):
    @commands.command(name="getguests")
    async def getGuests(self, ctx):
        await ctx.send("A")