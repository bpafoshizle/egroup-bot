import logging
import operator
import os

import aiohttp
import discord
from bs4 import BeautifulSoup
from cogs.utils.timing import calc_tomorrow_6am, wait_until
from discord.ext import commands, tasks

logger = logging.getLogger(__name__)


class WordOfTheDay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # pylint: disable=no-member
        self.wotd_task.start()

    @commands.command()
    async def wotd(self, ctx):
        wod = self.format_wod_response_embed(*await self.get_word_of_the_day())
        await ctx.send(embed=wod)

    @tasks.loop(hours=24)
    async def wotd_task(self):
        logger.info("channel id %s", os.getenv("DSCRD_CHNL_GENERAL"))
        chnl = self.bot.get_channel(int(os.getenv("DSCRD_CHNL_GENERAL")))
        logger.info("Got channel %s", chnl)
        await chnl.send(
            embed=self.format_wod_response_embed(*await self.get_word_of_the_day())
        )

    @wotd_task.before_loop
    async def before(self):
        await self.bot.wait_until_ready()
        logger.info("wotd_task_before_loop: bot ready")
        tmrw_6am = calc_tomorrow_6am()
        logger.info("wotd_task_before_loop: waiting until: %s", tmrw_6am)
        await wait_until(tmrw_6am)
        logger.info("wotd_task_before_loop: waited until 6am")

    async def get_word_of_the_day(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://www.merriam-webster.com/word-of-the-day"
            ) as r:
                if r.status == 200:
                    soup = BeautifulSoup(await r.text(), features="html.parser")
                    logger.debug(
                        "received response from https://www.merriam-webster.com/word-of-the-day"
                    )
                    word = soup.find("div", class_="word-and-pronunciation").h1.string
                    part_of_speech = soup.find("span", class_="main-attr").string
                    word_syllables = soup.find("span", class_="word-syllables").string
                    definitions = list(
                        map(
                            operator.attrgetter("text"),
                            soup.find(
                                "div", class_="wod-definition-container"
                            ).find_all("p", recursive=False),
                        )
                    )
                    return word, word_syllables, part_of_speech, definitions

    def format_wod_response_embed(
        self, word, word_syllables, part_of_speech, definitions
    ):
        embed = discord.Embed(
            title="Word of the Day Post",
            description="Step up your vocab",
            color=0x9D2235,
        )
        embed.add_field(name="Today's Word", value=word, inline=False)
        embed.add_field(name="Part of Speech", value=part_of_speech)
        embed.add_field(name="Syllables", value=word_syllables, inline=False)
        embed.add_field(name="Definition(s)", value=definitions)
        return embed
