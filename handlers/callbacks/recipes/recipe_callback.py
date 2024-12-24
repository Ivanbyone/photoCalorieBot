""" """
import datetime
import os

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, FSInputFile, LinkPreviewOptions
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from utils.FSM_states import FsmStates

from data.dbconnect import mongoBase
from markups.markups import keyboard

recipes = Router()


@recipes.callback_query(F.data == "button_recipe_analyse_pressed")
async def recipe_hello_message(call: CallbackQuery, state: FSMContext) -> None:
    """

    :param call:
    :return:
    """

    date = await mongoBase.check_recipe_subscription(tg_id=call.message.chat.id)
    if date == None or date < datetime.datetime.utcnow():
        await call.answer(text='У вас нет подписки.\n\nКупите подписку в разделе "Оплата".',
                          show_alert=True)
    else:
        keyboard = ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text="Куриная грудка 🐔")],
            [KeyboardButton(text="Фарш 🫔")],
            [KeyboardButton(text="Яйца 🍳")],
            [KeyboardButton(text="Овсянка 🥣")],
            [KeyboardButton(text="Тунец 🐠")],
            # [KeyboardButton(text="Морепродукты 🍤")],
            [KeyboardButton(text="Творог 🍚")],
            # [KeyboardButton(text="Лаваш/тортилья 🌮")],
            [KeyboardButton(text="Авокадо 🥑")],
            [KeyboardButton(text="Салаты и поке 🥗")],
            # [KeyboardButton(text="Пасты 🍝")],
            [KeyboardButton(text="Панкейки и вафли 🥞")],
            # [KeyboardButton(text="Сырники 🍮")],
            # [KeyboardButton(text="Роллы 🌯")],
            # [KeyboardButton(text="Вафли 🧇")],
            [KeyboardButton(text="Десерты 🍨")],
            [KeyboardButton(text="Назад")]
        ], resize_keyboard=True)

        await call.message.answer(text="Этот сборник рецептов представляет собой идеальное решение для тех, кто стремится к здоровому питанию без ущерба для вкуса. В каждой подборке вы найдете разнообразные блюда с рассчитанным КБЖУ, подходящие для любого времени года и любого повода — от повседневных завтраков до праздничных ужинов.\n\nКаждый рецепт не только вкусный, но и сбалансированный, что поможет вам легко контролировать свой рацион и достигать поставленных целей, будь то похудение, поддержание формы или просто стремление к более здоровому образу жизни. Благодаря простым и доступным ингредиентам вы сможете легко готовить блюда дома, наслаждаясь их разнообразием и изысканностью.\n\nПусть этот сборник станет вашим надежным помощником в кухне, вдохновляя на приготовление полезных и питательных блюд для себя и своих близких!",
                                  reply_markup=keyboard)

        await state.set_state(FsmStates.choose_category)


@recipes.message(F.text == "Десерты 🍨", StateFilter(FsmStates.choose_category))
async def send_desserts(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='desert2'),
            InlineKeyboardButton(text='➡️', callback_data='desert3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>Запеченные груши с творогом и рикоттой (КБЖУ: 383/24/12/28)</b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/YD18NMtn_v8?si=GuPBb-zWIUwMpHP7',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Куриная грудка 🐔", StateFilter(FsmStates.choose_category))
async def send_desserts(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='chicken2'),
            InlineKeyboardButton(text='➡️', callback_data='chicken3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="<b>Хрустящая курица в панировке (2 порции) (КБЖУ: 322/56/6/5)</b>",
                           parse_mode='html',
                           link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/7dny6Sww9a8?si=tYyIDI-o4QWO6z6W',
                                                                   prefer_large_media=True),
                           reply_markup=keyboard
                           )

    await state.clear()


@recipes.message(F.text == "Фарш 🫔", StateFilter(FsmStates.choose_category))
async def send_desserts(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='ground_meat2'),
            InlineKeyboardButton(text='➡️', callback_data='ground_meat3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="<b>Запеканка с помидорами и сыром (2 порции) (КБЖУ на порцию: 399/50/18/9,2)</b>",
                           parse_mode='html',
                           link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/kQSSgsBmQaE?si=FBiMRT-qEWAucTSa',
                                                                   prefer_large_media=True),
                           reply_markup=keyboard
                           )

    await state.clear()


@recipes.message(F.text == "Яйца 🍳", StateFilter(FsmStates.choose_category))
async def send_desserts(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='eggs2'),
            InlineKeyboardButton(text='➡️', callback_data='eggs3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="<b>Шакшука (КБЖУ: 417/22/21/34)</b>",
                           parse_mode='html',
                           link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/3O3BmiUW8Bg?si=kpBAgyaFNMApMoEj',
                                                                   prefer_large_media=True),
                           reply_markup=keyboard
                           )

    await state.clear()


@recipes.message(F.text == "Овсянка 🥣", StateFilter(FsmStates.choose_category))
async def send_desserts(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='oatmeal2'),
            InlineKeyboardButton(text='➡️', callback_data='oatmeal3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                           text="<b>ОВСЯНОБЛИН с арахисовой пастой и бананом (КБЖУ: 481/20/20/56)</b>",
                           parse_mode='html',
                           link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/Pou1GLei12s?si=7HsqBPAfxYps3Ivu',
                                                                   prefer_large_media=True),
                           reply_markup=keyboard
                           )

    await state.clear()


@recipes.message(F.text == "Творог 🍚", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='cheese2'),
            InlineKeyboardButton(text='➡️', callback_data='cheese3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>Творожные бейглы с ветчиной и сыром (КБЖУ: 398/38/15/28)</b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/qMQ6y1GWddE?si=1UAca8JalCdyT12s',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Роллы 🌯", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='roll2'),
            InlineKeyboardButton(text='➡️', callback_data='roll3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b> Цезарь ролл (КБЖУ: 429/31/15/41)</b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/0ib2rlox5fw?si=KM_3BLnnTIgPqeiC',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Авокадо 🥑", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='avocado2'),
            InlineKeyboardButton(text='➡️', callback_data='avocado3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>Сэндвич с авокадо ( КБЖУ: 417/20/27/27)</b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/Pg5HGQDrM4w?si=xvuYVbTG_KBO08Ug',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Тунец 🐠", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='tuna2'),
            InlineKeyboardButton(text='➡️', callback_data='tuna3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>ПОКЕ с рисом, тунцом и креветками (КБЖУ: 449/20/14/56) </b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/bF4_J4Y4oBY?si=mrQmEhjVxVF9hpak',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Салаты и поке 🥗", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='salads2'),
            InlineKeyboardButton(text='➡️', callback_data='salads3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>Салат с креветками, рукколой и киноа (КБЖУ: 316/20/10/35) </b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/TXynF6Ra008?si=6EgnV8l_oKmi3yN4',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Панкейки и вафли 🥞", StateFilter(FsmStates.choose_category))
async def send_cheese(message: Message, bot: Bot, state: FSMContext):
    """

    :return:
    """

    await bot.send_message(chat_id=message.from_user.id,
                           text="Воспользуйтесь кнопками меню и выберете то, что хотите приготовить 👇\n\n(чтобы посмотреть все рецепты в этом разделе, листайте вправо или влево⬅️➡️)",
                           parse_mode='html',
                           reply_markup=ReplyKeyboardRemove())

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes1')],
        [
            InlineKeyboardButton(text='⬅️', callback_data='pancakes2'),
            InlineKeyboardButton(text='➡️', callback_data='pancakes3')
        ],
        [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
    ])

    await bot.send_message(chat_id=message.from_user.id,
                         text="<b>Творожные оладьи с луком и сыром (КБЖУ: 352/26/15/25) </b>",
                         parse_mode='html',
                         link_preview_options=LinkPreviewOptions(url='https://youtube.com/shorts/fPugTMZVZ0k?si=KMR24MA6sE5xTl_u',
                                                                   prefer_large_media=True),
                         reply_markup=keyboard
                         )

    await state.clear()


@recipes.message(F.text == "Назад", StateFilter(FsmStates.choose_category))
async def home(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(chat_id=message.from_user.id, text='Возвращаюсь в главное меню...', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"И снова, здравствуй ✋\n\nЯ помогу тебе скинуть пару лишних килограмм и прийти к гармоничным отношениям с едой без отказа от любимых продуктов и не тратя много времени на готовку. Я проанализирую твой рацион, дам рекомендацию на уровне топового нутрициолога и помогу с быстрыми, вкусными и сбалансированными рецептами.",
                           parse_mode="html",
                           reply_markup=keyboard)

    await state.clear()
