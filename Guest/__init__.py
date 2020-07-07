from .guestcog import Guest

async def setup(bot):
    bot.add_cog(Guest(bot))
