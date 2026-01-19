def main():
    import logging
    import os

    from dotenv import find_dotenv, load_dotenv

    # Locate .env file specifically to ensure it loads from parent if needed
    dotenv_path = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path, override=True)

    # Set the logging level based on the environment variable.
    log_level = os.environ.get("LOGLEVEL", "INFO")
    log_level = log_level.upper()

    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        raise ValueError(
            "Invalid log level. Must be one of: "
            "DEBUG, INFO, WARNING, ERROR, CRITICAL"
        )

    logging.basicConfig(
        format="%(asctime)s %(levelname)-4s %(name)-25s %(message)s",
        level=getattr(logging, log_level),
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Silence discord library noise to focus on pydiscogs
    logging.getLogger("discord").setLevel(logging.WARNING)

    # NOW we can safely log things
    if dotenv_path:
        logging.info(f"Loading .env from: {dotenv_path}")
    else:
        logging.warning("No .env file found!")

    pg_url = os.environ.get("POSTGRES_DB_URL")
    logging.info(f"POSTGRES_DB_URL present: {bool(pg_url)}")

    logging.info(f"Current LOGLEVEL: {log_level}")

    from pydiscogs import botbuilder

    bot = botbuilder.build_bot("egroup-bot.yaml")
    logging.info("running bot: %s", bot)
    bot.run(bot.discord_token)


if __name__ == "__main__":
    main()
