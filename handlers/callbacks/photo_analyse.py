""" Callbacks handlers """

import os
import asyncio

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from utils.FSM_states import FsmStates
from gpt.requests_gpt import gpt
from data.dbconnect import mongoBase
from markups.markups import keyboard

photo_analyse = Router()


@photo_analyse.callback_query(F.data == "button_photo_analyse_pressed")
async def photo_analyse_callback(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    subscription = await mongoBase.check_photo_attempts(tg_id=call.message.chat.id)
    profile = await mongoBase.send_profile(tg_id=call.message.chat.id)


    if subscription == None or subscription <= 0:
        await call.answer(text='У вас нет попыток.\n\nКупите попытки в разделе "Оплата".',
                          show_alert=True)
    elif profile["gender"] == "Не указан" or profile["age"] == "Не указан" or profile["weight"] == "Не указан" or profile["height"] == "Не указан" or profile["target"] == "Не указан":
        await call.answer(text='У вас не указаны физиологические параметры.\n\nПерейдите в профиль и укажите параметры',
                          show_alert=True)
    else:
        await call.message.delete()

        await call.message.answer("Отправь мне фото, и я посмотрю, что у тебя на тарелке!\nМожешь просто описать текстом, и я помогу рассчитать калорийность и макронутриенты. Если не знаешь, что съесть, загляни во вкладку с рецептами 😉")

        await state.set_state(FsmStates.send_photo)


@photo_analyse.message(StateFilter(FsmStates.send_photo), F.photo)
async def user_send_photo(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"<i>Запрос обрабатывается...</i>",
                                 parse_mode="html")

    photo = message.photo[-1]
    destination = os.path.abspath(f"photo/file{message.from_user.id}.jpg")
    await bot.download(file=photo.file_id, destination=destination)

    await bot.send_chat_action(chat_id=message.from_user.id, action="typing")

    data = dict(await mongoBase.send_profile(tg_id=message.from_user.id))

    manBMR = 88.36 + (13.4 * int(data["weight"])) + (4.8 * int(data["height"])) - (5.7 * int(data["age"]))
    womanBMR = 447.6 + (9.2 * int(data["weight"])) + (3.1 * int(data["height"])) - (4.3 * int(data["age"]))

    if data["gender"] == "Мужчина":
        res = await gpt.analyse_photo(image=destination, gender=data["gender"], age=data["age"], height=data["height"], target=data["target"], calorie=manBMR * 1.5)
    else:
        res = await gpt.analyse_photo(image=destination, gender=data["gender"], age=data["age"], height=data["height"],
                                      target=data["target"], calorie=womanBMR * 1.5)

    await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
    print(res)

    os.remove(destination)

    await mongoBase.update_attempts(message.from_user.id)

    await msg.delete()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Результат:\n\n{res.message.content}",
                           parse_mode="html")

    await state.clear()

    await asyncio.sleep(5)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Я помогу тебе скинуть пару лишних килограмм и прийти к гармоничным отношениям с едой без отказа от любимых продуктов и не тратя много времени на готовку. Я проанализирую твой рацион, дам рекомендацию на уровне топового нутрициолога и помогу с быстрыми, вкусными и сбалансированными рецептами.",
                           parse_mode="html",
                           reply_markup=keyboard)


@photo_analyse.message(StateFilter(FsmStates.send_photo))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """
    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректный формат фотографии.\n\nПопробуйте снова.")

    await asyncio.sleep(0.7)

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"И снова, здравствуй ✋\n\nЯ помогу тебе скинуть пару лишних килограмм и прийти к гармоничным отношениям с едой без отказа от любимых продуктов и не тратя много времени на готовку. Я проанализирую твой рацион, дам рекомендацию на уровне топового нутрициолога и помогу с быстрыми, вкусными и сбалансированными рецептами.",
                           parse_mode="html",
                           reply_markup=keyboard)
