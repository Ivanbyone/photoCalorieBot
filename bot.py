""" Starting bot """

import asyncio
import logging

from config.config import bot, dp
from handlers.main_commands import commands
from handlers.callbacks import callback
from utils.command_helper import set_commands

bot_logger = logging.getLogger(__name__)

async def main() -> None:
    """
    function for starting bot
    :return: None
    """

    # Config for logging events
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Level info for starting Bot
    bot_logger.info('Bot has been started...')

    dp.include_routers(
        commands.router,
        callback.callbacks
    )

    dp.startup.register(set_commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Starting bot failed with {e}")
