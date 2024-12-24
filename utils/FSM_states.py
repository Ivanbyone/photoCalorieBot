""" """

from aiogram.fsm.state import State, StatesGroup


class FsmStates(StatesGroup):

    send_photo = State()
    choose_gender = State()
    choose_age = State()
    choose_weight = State()
    choose_height = State()
    choose_target = State()
    choose_category = State()
    pay_photos = State()
