""" """

from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from markups.markups import keyboard_profile
from data.dbconnect import mongoBase
from utils.FSM_states import FsmStates

profile = Router()


@profile.callback_query(F.data == 'profile_button_pressed')
async def show_profile(call: CallbackQuery) -> None:
    """

    :param call:
    :return: None
    """
    profile = dict(await mongoBase.send_profile(call.from_user.id))

    await call.message.edit_text(text=f"Ваш профиль:\n\n{profile['role']}\nid: {profile['telegramId']}\nИмя: {profile['userName']}\nКоличество попыток: {profile['attempts']}\nДата регистрации: {profile['registerDate']}\nПол: {profile['gender']}\nВозраст: {profile['age']}\nВес: {profile['weight']}\nРост: {profile['height']}\nЦель: {profile['target']}",
                                 parse_mode="html",
                                 reply_markup=keyboard_profile)


@profile.callback_query(F.data == "button_edit_profile")
async def edit_profile(call: CallbackQuery) -> None:
    """

    :param call:
    :return: None
    """

    # Keyboard for user's profile changing
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Пол', callback_data='choose_gender')],
        [InlineKeyboardButton(text='Возраст', callback_data='choose_age')],
        [InlineKeyboardButton(text='Вес', callback_data='choose_weight')],
        [InlineKeyboardButton(text='Рост', callback_data='choose_height')],
        [InlineKeyboardButton(text='Цель', callback_data='choose_target')],
        [InlineKeyboardButton(text='Назад', callback_data='profile_button_pressed')]
    ]
    )

    await call.message.edit_text(text=f"Выбери поле, которое хочешь редактировать",
                                 parse_mode='html',
                                 reply_markup=keyboard)


@profile.callback_query(F.data == 'choose_gender', StateFilter(default_state))
async def choose_gender(call: CallbackQuery, state: FSMContext) -> None:
    """
    Function for choosing gender
    :param call: type CallbackQuery
    :return: None
    """

    await call.message.delete()

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Мужчина")],
        [KeyboardButton(text="Женщина")]
    ], one_time_keyboard=True,
    resize_keyboard=True)

    await call.message.answer(text=f"Выбери свой пол",
                                 parse_mode='html',
                                 reply_markup=keyboard)

    await state.set_state(FsmStates.choose_gender)


@profile.message(StateFilter(FsmStates.choose_gender), F.text.in_({"Мужчина", "Женщина"}))
async def change_gender(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """

    await mongoBase.change_gender(tg_id=message.from_user.id, gender=message.text)

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Твой пол успешно записан!",
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Возвращайся в профиль",
                           reply_markup=keyboard)


@profile.message(StateFilter(FsmStates.choose_gender))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :return:
    """
    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректно выбран пол.\n\nВыбери значение из предложенных.")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Вернись в профиль и попробуй снова",
                           reply_markup=keyboard)


@profile.callback_query(F.data == 'choose_age', StateFilter(default_state))
async def choose_age(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    await call.message.answer(text=f"Напиши свой возраст в числовом формате",
                              parse_mode='html')

    await state.set_state(FsmStates.choose_age)


@profile.message(StateFilter(FsmStates.choose_age), F.text.isdigit())
async def change_age(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param state:
    :return:
    """

    await mongoBase.change_age(tg_id=message.from_user.id, age=message.text)

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Твой возраст успешно записан!")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Возвращайся в профиль",
                           reply_markup=keyboard)


@profile.message(StateFilter(FsmStates.choose_age))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :return:
    """
    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректно введен возраст.\n\nУкажи значение возраста в числовом формате.")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Вернись в профиль и попробуй снова",
                           reply_markup=keyboard)


@profile.callback_query(F.data == 'choose_weight', StateFilter(default_state))
async def choose_weight(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    await call.message.answer(text=f"Напиши свой вес в числовом формате",
                              parse_mode='html')

    await state.set_state(FsmStates.choose_weight)


@profile.message(StateFilter(FsmStates.choose_weight), F.text.isdigit())
async def change_weight(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """

    await mongoBase.change_weight(tg_id=message.from_user.id, weight=message.text)

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Твой вес успешно записан!")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Возвращайся в профиль",
                           reply_markup=keyboard)


@profile.message(StateFilter(FsmStates.choose_weight))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :return:
    """

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректно введен вес.\n\nУкажи значение веса в числовом формате.")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Вернись в профиль и попробуй снова",
                           reply_markup=keyboard)


@profile.callback_query(F.data == 'choose_height', StateFilter(default_state))
async def choose_height(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    await call.message.answer(text=f"Напиши свой рост в числовом формате",
                              parse_mode='html')

    await state.set_state(FsmStates.choose_height)


@profile.message(StateFilter(FsmStates.choose_height), F.text.isdigit())
async def change_height(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """

    await mongoBase.change_height(tg_id=message.from_user.id, height=message.text)

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Твой вес успешно записан!")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Возвращайся в профиль",
                           reply_markup=keyboard)


@profile.message(StateFilter(FsmStates.choose_height))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :return:
    """

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректно введен рост.\n\nУкажи значение роста в числовом формате.")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Вернись в профиль и попробуй снова",
                           reply_markup=keyboard)


@profile.callback_query(F.data == 'choose_target', StateFilter(default_state))
async def choose_target(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    await call.message.delete()

    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Похудеть")],
        [KeyboardButton(text="Поддержание")],
        [KeyboardButton(text="Набор веса")]
    ], one_time_keyboard=True,
        resize_keyboard=True)

    await call.message.answer(text=f"Выбери свою цель из предложенных",
                              parse_mode='html',
                              reply_markup=keyboard)

    await state.set_state(FsmStates.choose_target)


@profile.message(StateFilter(FsmStates.choose_target), F.text.in_({"Похудеть", "Поддержание", "Набор веса"}))
async def change_target(message: Message, bot: Bot, state: FSMContext) -> None:
    """

    :param message:
    :param bot:
    :param state:
    :return:
    """

    await mongoBase.change_target(tg_id=message.from_user.id, target=message.text)

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text=f"Твоя цель успешно записана!")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Возвращайся в профиль",
                           reply_markup=keyboard)


@profile.message(StateFilter(FsmStates.choose_target))
async def not_age(message: Message, bot: Bot, state: FSMContext):
    """

    :param message:
    :param bot:
    :return:
    """

    await state.clear()

    await bot.send_message(chat_id=message.from_user.id,
                           text="Некорректно выбрана цель.\n\nВыбери цель из предложенных.")

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data='button_edit_profile')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="Вернись в профиль и попробуй снова",
                           reply_markup=keyboard)
