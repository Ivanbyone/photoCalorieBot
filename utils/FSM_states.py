""" """

from aiogram.fsm.state import State, StatesGroup


class FSMPhoto(StatesGroup):

    send_photo = State()
