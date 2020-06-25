from .diamantecog import Diamante

async def setup(bot):
    bot.add_cog(Diamante(bot))
