""" Main commands """

import random
import time

from aiogram import Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import text

from markups.markups import keyboard
from bot import bot_logger

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, bot: Bot) -> None:
    """
    Handler for /start command
    :param message: aiogram type class Message
    :param bot: aiogram class Bot
    :return: None
    """

    bot_logger.info("Command start pressed!")

    start_stickers = [
        r"CAACAgIAAxkBAAELT7Blvrn134vxH3rbovLj7TwGg-5RtgACRQMAArVx2gaTiBAcidwNGzQE",
        r"CAACAgIAAxkBAAELT7dlvr0QUV-K0cDHRSBcDccAAafif74AAvcBAAIWQmsKOfZwb7Rjf8Q0BA",
        r"CAACAgIAAxkBAAELT8llvsPPiy9czTDfQbzcaYWRrHhD9QACrzIAAhnpSEp0UfL43ZZrSTQE",
        r"CAACAgIAAxkBAAELT8VlvsNwIxOQ6loaxw86y1gOnn5pqwAChAADrWW8FEXv16BtLIaKNAQ",
        r"CAACAgIAAxkBAAELT8NlvsNZHmoRsEKo7kIa0Im4hQHVQQAC9Q8AArsgIUjI0a78icEg7jQE",
        r"CAACAgIAAxkBAAELT8FlvsNKSaWvc4-0riuW26zV8-ctjwACTwADrWW8FGuRHI2HrK-TNAQ",
        r"CAACAgIAAxkBAAELT79lvsNEjhj3RS6hQBuj5jdiS3gIbgAC0Q0AAstxcEvO1r8zXvNYlzQE",
        r"CAACAgIAAxkBAAELT71lvsM9l6KxxYF4n6Tw2a3Na1HrzQACggADpsrIDJxaB_KcQQRnNAQ",
        r"CAACAgIAAxkBAAELT7tlvsM3sQWhvo-P-ntgJMffI_9I-AACbwAD9wLID-kz_ZsHgo4yNAQ",
        r"CAACAgIAAxkBAAELT7llvsMxV_5CcFYxCSdEYaEVWKizGQACbgADwDZPE22H7UqzeJmXNAQ"
    ]

    msg = await bot.send_sticker(chat_id=message.from_user.id,
                                 sticker=random.choice(start_stickers))

    time.sleep(1)

    await msg.delete()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Привет, <b>{message.from_user.full_name}</b> ✋\n\nЯ определю калорийность твоего рациона по фото и дам рекомендации на уровне топового нутрициолога. С моей помощью ты также сможешь проанализировать свой собственный рецепт 😎\n\nВНИМАНИЕ: бесплатный доступ к боту дается на 2 дня!",
                           parse_mode="html",
                           reply_markup=keyboard)


@router.message(Command("help"))
async def start_handler(message: Message, bot: Bot) -> None:
    """
    Help command for users with some info about bot functions
    :param message: aiogram type class Message
    :param bot: aiogram class Bot
    :return: None
    """

    help_msg = text(
        "Мой функционал:\n\n",
        "/start - перезапуск бота\n",
        "/help - посмотреть возможности и доступный функционал\n",
        "/profile - посмотреть Ваш профиль"
    )

    await bot.send_message(chat_id=message.from_user.id,
                           text=help_msg,
                           parse_mode="html")


@router.message(Command("profile"))
async def start_handler(message: Message, bot: Bot) -> None:
    """
    Show user profile
    :param message: aiogram type class Message
    :param bot: aiogram class Bot
    :return: None
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Ваш профиль:",
                           parse_mode="html")
