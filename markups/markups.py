""" All markups """

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_photo_analyse = InlineKeyboardButton(
    text='🥗 Анализатор по фото',
    callback_data='big_button_1_pressed'
)

button_recipe_analyse = InlineKeyboardButton(
    text='🌮 Анализатор рецепта',
    callback_data='big_button_2_pressed'
)

button_buy_premium = InlineKeyboardButton(
    text='🥑 Купить премиум версию',
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

button_peach_recipes_bot = InlineKeyboardButton(
    text='🤩 Лучшие рецепты с КБЖУ',
    callback_data='big_button_6_pressed',
    url='https://t.me/lisa_peach1_recipes_bot'
)

button_developer_profile = InlineKeyboardButton(
    text='👨‍💻 Разработка ботов',
    callback_data='developer_button_pressed',
    url='https://t.me/ivanbyone'
)

# Сreating object of inline keyboard
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_photo_analyse],
                     [button_recipe_analyse],
                     [button_buy_premium],
                     [button_support],
                     [button_profile],
                     [button_peach_recipes_bot],
                     [button_developer_profile]]
)
