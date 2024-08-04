import asyncio
import importlib

from pyrogram import idle

from StringGen import LOGGER, Vashu
from StringGen.modules import ALL_MODULES


async def string_boot():
    try:
        await string.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("StringGen.modules." + all_module)

    LOGGER.info(f"@{Vashu.username} Started.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(string_boot())
    LOGGER.info("Stopping String Gen Bot...")
