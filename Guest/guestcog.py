from redbot.core import commands

class Guest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="getguests")
    async def getGuests(self, ctx, server):
        for member in server.members:
            for role in member.roles: 
                if role.id == 730173883151286285:
                    await ctx.send("a")