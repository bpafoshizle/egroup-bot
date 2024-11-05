def main():
    import logging
    import os

    # Set the logging level based on the environment variable
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_level = log_level.upper()

    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError(
            "Invalid log level. Must be one of: DEBUG, INFO, WARNING, ERROR, CRITICAL"
        )

    logging.basicConfig(
        format="%(asctime)s %(levelname)-4s %(name)-25s %(message)s",
        level=getattr(logging, log_level),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    from pydiscogs import botbuilder

    bot = botbuilder.build_bot("egroup-bot.yaml")
    logging.info("running bot: %s", bot)
    bot.run(bot.discord_token)


if __name__ == "__main__":
    main()
