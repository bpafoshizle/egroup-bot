import logging
import os

from discord.ext import commands
from pydiscogs import botbuilder

bot = botbuilder.build_bot('egroup-bot.yaml')

logging.info("running bot: %s", bot)
bot.run(bot.discord_token)
