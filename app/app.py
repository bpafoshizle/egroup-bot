import logging
import os

from discord.ext import commands
from pydiscogs.inspire import InspireQuote
from pydiscogs.reddit import Reddit
from pydiscogs.stocks import StockQuote
from pydiscogs.twitch import Twitch
from pydiscogs.wotd import WordOfTheDay

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
logging.basicConfig(level=LOGLEVEL)

guild_id = os.getenv("DISCORD_GUILD_ID")
guild_ids = [int(guild_id)] if guild_id else None

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    logging.info("Logged in as %s", bot.user)


@bot.slash_command(guild_ids=guild_ids)
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


bot.add_cog(WordOfTheDay(bot, guild_ids, os.getenv("DSCRD_CHNL_GENERAL")))
bot.add_cog(InspireQuote(bot, guild_ids))
bot.add_cog(
    StockQuote(
        bot,
        guild_ids=guild_ids,
        stock_list=[
            "SPY",
            "QQQ",
            "GME",
            "IJR",
            "BTC-USD",
            "ETC-USD",
        ],
        polygon_token=os.getenv("POLYGON_TOKEN"),
        discord_post_channel_id=os.getenv("DSCRD_CHNL_MONEY"),
    )
)
bot.add_cog(
    Twitch(
        bot,
        guild_ids,
        os.getenv("TWITCH_BOT_CLIENT_ID"),
        os.getenv("TWITCH_BOT_CLIENT_SECRET"),
        os.getenv("DSCRD_CHNL_GAMING"),
        join_channels_list=[
            "bpafoshizle",
            "ephenry84",
            "elzblazin",
            "kuhouseii",
        ]
    )
)
bot.add_cog(
    Reddit(
        bot=bot,
        guild_ids=guild_ids,
        reddit_client_id=os.getenv("REDDIT_CLIENT_ID"),
        reddit_client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        reddit_username=os.getenv("REDDIT_USERNAME"),
        reddit_password=os.getenv("REDDIT_PASSWORD"),
        subreddit_list=["getmotivated", "todayilearned", "interestingasfuck"],
        gfycat_client_id=os.getenv("GFYCAT_CLIENT_ID"),
        gfycat_client_secret=os.getenv("GFYCAT_CLIENT_SECRET"),
        discord_post_channel_id=os.getenv("DSCRD_CHNL_GENERAL"),
    )
)

logging.info("running bot: %s", bot)
bot.run(os.getenv("DISCORD_TOKEN"))
