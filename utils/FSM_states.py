""" """

from aiogram.fsm.state import State, StatesGroup


class FsmStates(StatesGroup):

    send_photo = State()
    send_recipe = State()
