""" Starting bot """

import asyncio

from aiogram import Bot, Dispatcher

from config.config import token
from handlers.main_commands import commands

bot = Bot(token=token)
dp = Dispatcher()


async def main() -> None:
    """
    function for starting bot
    :return: None
    """

    dp.include_routers(
        commands.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Starting bot failed with {e}")
