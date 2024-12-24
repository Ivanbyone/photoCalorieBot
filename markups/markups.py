""" All markups """

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_photo_analyse = InlineKeyboardButton(
    text='🥗 Анализ по фото',
    callback_data='button_photo_analyse_pressed'
)

button_recipe_analyse = InlineKeyboardButton(
    text='🌮 Рецепты с КБЖУ',
    callback_data='button_recipe_analyse_pressed'
)

button_info = InlineKeyboardButton(
    text='🔥 Пошаговый план + трекер',
    callback_data='big_button_3_pressed'
)

button_support = InlineKeyboardButton(
    text='✍️ Поддержка',
    callback_data='big_button_4_pressed',
    url='https://t.me/PhotoCalorieSupport'
)

button_profile = InlineKeyboardButton(
    text='👤 Профиль',
    callback_data='profile_button_pressed'
)

button_pay = InlineKeyboardButton(
    text='⭐ Оплата',
    callback_data='pay_button_pressed'
)

button_developer_profile = InlineKeyboardButton(
    text='🤔 Как пользоваться ботом?',
    callback_data='developer_button_pressed'
)

button_back = InlineKeyboardButton(
    text='Назад',
    callback_data='/start'
    # url='https://t.me/photo_calorie_bot?start=xxx'
)

button_edit_profile = InlineKeyboardButton(
    text='Редактировать профиль',
    callback_data='button_edit_profile'
)

button_choose_gender = InlineKeyboardButton(
    text='Выбрать пол',
    callback_data='choose_gender'
)

# Сreating objects of inline keyboard
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_photo_analyse],
                     [button_recipe_analyse],
                     [button_info],
                     [button_profile],
                     [button_pay],
                     [button_developer_profile],
                     [button_support]]
)

keyboard_profile = InlineKeyboardMarkup(
    inline_keyboard=[[button_edit_profile],
                     [button_back]]
)

keyboard_edit_profile = InlineKeyboardMarkup(
    inline_keyboard=[[button_choose_gender],
                     [button_back]]
)
