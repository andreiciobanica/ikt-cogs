from .notificareyt import Notificare

async def setup(bot):
    bot.add_cog(Notificare(bot))
