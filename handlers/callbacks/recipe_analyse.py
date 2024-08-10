""" """

import time

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, PhotoSize
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from utils.FSM_states import FsmStates
from gpt.requests_gpt import recipe_to_gpt

recipe_analyse = Router()


@recipe_analyse.callback_query(F.data == "button_recipe_analyse_pressed", StateFilter(default_state))
async def photo_analyse_callback(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    await call.message.answer("Я помогу тебе рассчитать КБЖУ сложного блюда. Для этого напиши мне какие ингридиенты ты используешь и в каком количестве, а также укажи количество порций.")

    await state.set_state(FsmStates.send_recipe)


@recipe_analyse.message(StateFilter(FsmStates))
async def user_send_recipe(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"<i>Запрос обрабатывается...</i>",
                                 parse_mode="html")

    gpt_response = recipe_to_gpt(text=message.text)

    await msg.delete()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Результат по вашему запросу:\n\n{gpt_response}",
                           parse_mode="html")

    await state.clear()
