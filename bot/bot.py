import nextcord
import os
from nextcord.ext import commands, tasks
import importlib.util
import importlib.machinery
from random import choice


class Bot(commands.Bot):
    def __init__(self, token: str):
        intents = nextcord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix=self.prefix, intents=intents, help_command=None)

    def initialize(self, token):
        print("Starting bot...")

        self.load_extensions()
        self.run(token)

    def load_extensions(self):
        for f in os.listdir("./cogs"):
            for cog in os.listdir(f"./cogs/{f}"):
                if cog.endswith(".py"):
                    try:
                        module = importlib.import_module(f"cogs.{cog[:-3]}")

                        self.load_extension(name=f"cogs.{cog[:-3]}")
                        print(f"Loaded {cog[:-3]} cog")

                    except Exception as e:
                        print(
                            f"Failed to load cog {cog[:-3]}. Traceback:\n\n{str(e)}")
                        continue

    def prefix(self, bot, message: nextcord.Message):
        # self.db.get
        guilddata = None  # self.db.get_guild_data(message.guild.id)[0]
        return guilddata.prefix if guilddata else "!"

    async def on_ready(self):
        print(f"logged in as {self.user.name} ({self.user.id})")

        self.update_presence.start()

    @tasks.loop(seconds=5)
    async def update_presence(self):
        await self.wait_until_ready()

        await self.change_presence(
            status=nextcord.Status.online,
            activity=nextcord.Activity(
                type=nextcord.ActivityType.playing, name=choice(
                    ["Muting", "Banning", "Kicking", "Deleting Messages", "Unmuting", "Unbanning", "Moderating"])
            ))
