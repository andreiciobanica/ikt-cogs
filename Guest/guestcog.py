from redbot.core import commands

class Diamante(commands.Cog):
    @commands.command(name="getguests")
    async def getGuests(self, ctx):
        for member in server.members:
            for role in member.roles: 
                if role.id == "730173883151286285":
                    await ctx.send("A")