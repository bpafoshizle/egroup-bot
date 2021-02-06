import json
import logging
import operator
import os
import asyncio
import datetime

# import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands, tasks

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)

bot = commands.Bot(command_prefix=".")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


def get_word_of_the_day():
    response = requests.get("https://www.merriam-webster.com/word-of-the-day")
    soup = BeautifulSoup(response.text, features="html.parser")
    logging.debug(
        "received response from https://www.merriam-webster.com/word-of-the-day"
    )
    word = soup.find("div", class_="word-and-pronunciation").h1.string
    part_of_speech = soup.find("span", class_="main-attr").string
    word_syllables = soup.find("span", class_="word-syllables").string
    definitions = list(
        map(
            operator.attrgetter("text"),
            soup.find("div", class_="wod-definition-container").find_all(
                "p", recursive=False
            ),
        )
    )

    return word, word_syllables, part_of_speech, definitions


def format_wod_response_text(word, word_syllables, part_of_speech, definitions):
    nln = "\n"
    wod_response = f"""\
Word of the day: {word} [{word_syllables}], {part_of_speech}
Definitions:
{nln.join(definitions)}"""
    return wod_response


def format_wod_response_embed(word, word_syllables, part_of_speech, definitions):
    pass


async def wait_until(dt):
    # sleep until the specified datetime
    now = datetime.datetime.now()
    await asyncio.sleep((dt - now).total_seconds())


def calc_tomorrow_6am():
    tmrw_6am = datetime.datetime.now() + datetime.timedelta(days=1)
    tmrw_6am = tmrw_6am.replace(hour=6, minute=0, second=0, microsecond=0)
    return tmrw_6am


@bot.event
async def on_ready():
    logging.info("Logged in as %s", bot.user)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def inspire(ctx):
    await ctx.send(get_quote())


@bot.command()
async def wotd(ctx):
    wod = format_wod_response_text(*get_word_of_the_day())
    await ctx.send(wod)


@tasks.loop(hours=24)
async def wotd_task():
    logging.info("channel id %s", os.getenv("DSCRD_CHNL_GENERAL"))
    chnl = bot.get_channel(int(os.getenv("DSCRD_CHNL_GENERAL")))
    logging.info("Got channel %s", chnl)
    await chnl.send(format_wod_response_text(*get_word_of_the_day()))


@wotd_task.before_loop
async def before():
    await bot.wait_until_ready()
    logging.info("wotd_task_before_loop: bot ready")
    tmrw_6am = calc_tomorrow_6am()
    logging.info("wotd_task_before_loop: waiting until: %s", tmrw_6am)
    await wait_until(tmrw_6am)
    logging.info("wotd_task_before_loop: waited until 6am")


# Start tasks
wotd_task.start()

logging.info("running bot: %s", bot)
bot.run(os.getenv("DISCORD_TOKEN"))
