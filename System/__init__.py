from .lideri import lideri_grade

async def setup(bot):
    bot.add_cog(lideri_grade(bot))
