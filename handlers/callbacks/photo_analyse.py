""" Callbacks handlers """
import time

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, PhotoSize
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from utils.FSM_states import FSMPhoto

photo_analyse = Router()


@photo_analyse.callback_query(F.data == "big_button_1_pressed", StateFilter(default_state))
async def photo_analyse_callback(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    await call.message.answer("Отправьте фото вашего блюда!")

    await state.set_state(FSMPhoto.send_photo)


@photo_analyse.message(StateFilter(FSMPhoto), F.photo[-1].as_('largest_photo'))
async def user_send_photo(message: Message, bot: Bot, state: FSMContext, largest_photo: PhotoSize) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :param largest_photo:
    :return:
    """

    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=f"<i>Запрос обрабатывается...</i>",
                                 parse_mode="html")

    time.sleep(2)

    photo = message.photo[0].file_id
    file_info = await bot.get_file(photo)
    print(f'file_path: {file_info.file_path}')

    await msg.delete()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Результат:",
                           parse_mode="html")

    await state.clear()
