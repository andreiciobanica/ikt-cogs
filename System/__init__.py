import json
from pathlib import Path
from .lideri import TempRole
from .lideri import lideri_grade

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]

async def setup(bot):
    bot.add_cog(lideri_grade(bot))
    bot.add_cog(TempRole(bot))
