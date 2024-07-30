""" Set commands' helper panel"""

from aiogram.types import BotCommand
from aiogram import Bot


async def set_commands(bot: Bot):

    bot_commands = [
        BotCommand(command="/start", description="Перезапустить бота"),
        BotCommand(command="/help", description="Посмотреть возможности бота"),
        BotCommand(command="/profile", description="Посмотреть Ваш профиль")
    ]

    await bot.set_my_commands(bot_commands)
