import nextcord
from bot import Bot


class OnGuildJoin(nextcord.Cog):
    def __init__(self, client: Bot):
        self.cient = client

    @nextcord.Cog.listener()
    async def on_guild_join(self, guild: nextcord.Guild):
        # Create base guild data, if none exists
        pass


def setup(client: Bot):
    client.add_cog(OnGuildJoin(client=client))
