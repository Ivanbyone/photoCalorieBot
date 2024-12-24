""" Main commands """

import asyncio
import datetime
import random

from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import text
from aiogram.fsm.context import FSMContext

from markups.markups import keyboard
from bot import bot_logger
from data.dbconnect import mongoBase

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, bot: Bot, state: FSMContext) -> None:
    """
    Handler for /start command
    :param message: aiogram type class Message
    :param bot: aiogram class Bot
    :return: None
    """

    await state.clear()

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
                                 sticker=random.choice(start_stickers),
                                 reply_markup=ReplyKeyboardRemove())

    validate = await mongoBase.send_profile(message.from_user.id)

    bot_logger.info(f"Validation was carried out for {message.from_user.id}")

    if validate == None:

        bot_logger.info("User is not authorized!")

        date = datetime.datetime.utcnow().isoformat()

        await mongoBase.insert_user_to_base(tg_id=message.from_user.id,
                                            username=message.from_user.full_name,
                                            attempts=0,
                                            register_date=date,
                                            role="user",
                                            gender="Не указан",
                                            age="Не указан",
                                            weight="Не указан",
                                            height="Не указан",
                                            target="Не указана"
                                            )

        bot_logger.info(f"User with {message.from_user.id} was created in database!")

        await asyncio.sleep(1)

        await msg.delete()

        await bot.send_message(chat_id=message.from_user.id,
                               text=f"Привет! Я дам тебе пошаговый план как скинуть лишние килограммы и прийти к гармоничным отношениям с едой без отказа от любимых продуктов 🔥. А также проанализирую твой рацион по фото и помогу с вкусными и сбалансированными рецептами, которые помогут тебе достичь своей цели 🤓",
                               parse_mode="html",
                               reply_markup=keyboard)

        await bot.delete_message(message.chat.id, message.message_id)

    else:

        bot_logger.info("User is authorized!")

        await asyncio.sleep(1.2)

        await msg.delete()

        await bot.send_message(chat_id=message.from_user.id,
                               text=f"И снова, здравствуй ✋\n\nЯ дам тебе пошаговый план как скинуть лишние килограммы и прийти к гармоничным отношениям с едой без отказа от любимых продуктов 🔥. А также проанализирую твой рацион по фото и помогу с вкусными и сбалансированными рецептами, которые помогут тебе достичь своей цели 🤓",
                               parse_mode="html",
                               reply_markup=keyboard)

        await asyncio.sleep(0.8)

        await bot.delete_message(message.chat.id, message.message_id)


@router.callback_query(F.data == "/start")
@router.callback_query(F.data == "start_msg")
async def start(call: CallbackQuery) -> None:
    """

    :param call:
    :return:
    """
    if call.data == "/start":
        await call.message.edit_text(
                               text=f"Привет! Я дам тебе пошаговый план как скинуть лишние килограммы и прийти к гармоничным отношениям с едой без отказа от любимых продуктов 🔥. А также проанализирую твой рацион по фото и помогу с вкусными и сбалансированными рецептами, которые помогут тебе достичь своей цели 🤓",
                               parse_mode="html",
                               reply_markup=keyboard)
    else:
        await call.message.answer(
                               text=f"Привет! Я дам тебе пошаговый план как скинуть лишние килограммы и прийти к гармоничным отношениям с едой без отказа от любимых продуктов 🔥. А также проанализирую твой рацион по фото и помогу с вкусными и сбалансированными рецептами, которые помогут тебе достичь своей цели 🤓",
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

    bot_logger.info(f"Help message for {message.from_user.id}")

    await bot.send_message(chat_id=message.from_user.id,
                           text=help_msg,
                           parse_mode="html",
                           reply_markup=ReplyKeyboardRemove())


@router.message(Command("profile"))
async def start_handler(message: Message, bot: Bot) -> None:
    """
    Show user profile
    :param message: aiogram type class Message
    :param bot: aiogram class Bot
    :return: None
    """

    profile = dict(await mongoBase.send_profile(message.from_user.id))

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Ваш профиль:\n\n{profile['role']}\nid: {profile['telegramId']}\nИмя: {profile['userName']}\nКоличество попыток: {profile['attempts']}\nДата регистрации: {profile['registerDate']}",
                           parse_mode="html")
