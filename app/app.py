def main():
    import logging

    logging.basicConfig(
        format="%(asctime)s %(levelname)-4s %(name)-25s %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    from pydiscogs import botbuilder

    bot = botbuilder.build_bot("egroup-bot.yaml")
    logging.info("running bot: %s", bot)
    bot.run(bot.discord_token)


if __name__ == "__main__":
    main()
