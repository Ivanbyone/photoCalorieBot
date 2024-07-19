""" Main commands """

import random

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot import bot

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:

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

    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=random.choice(start_stickers))
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Привет, <b>{message.from_user.full_name}</b> ✋\n\nЯ бот, который умеет определять калорийность твоего приема пищи по фото и давать рекомендации на уровне топового нутрициолога, а также поможет тебе проанализировать твой собственный рецепт.\n\nВНИМАНИЕ: доступ к боту дается на 2 дня!",
                           parse_mode="html")
