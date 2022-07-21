from .perms import permisiuni

async def setup(bot):
    bot.add_cog(permisiuni(bot))
