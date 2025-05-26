import os
from bot import Bot
from constants import TOKEN


os.chdir("./")

if __name__ == "__main__":
    bot = Bot()
    bot.initialize(TOKEN)
