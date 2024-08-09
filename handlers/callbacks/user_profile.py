""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from data.db_commands import send_profile

profile = Router()


@profile.callback_query(F.data == "profile_button_pressed")
async def show_profile(call: CallbackQuery):
    """

    :param call:
    :return:
    """

    await call.message.delete()

    profile = dict(await send_profile(call.from_user.id))

    await call.message.answer(text=f"Ваш профиль:\n\n{profile['role']}\nid: {profile['telegramId']}\nИмя: {profile['userName']}\nКоличество попыток: {profile['attempts']}\nДата регистрации: {profile['registerDate']}",
                              parse_mode="html")
