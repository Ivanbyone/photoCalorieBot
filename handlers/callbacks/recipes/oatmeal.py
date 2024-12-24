""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'oatmeal5')
@router.callback_query(F.data == 'oatmeal4')
@router.callback_query(F.data == 'oatmeal3')
@router.callback_query(F.data == 'oatmeal2')
@router.callback_query(F.data == 'oatmeal1')
@router.callback_query(F.data == 'oatmeal_inline5')
@router.callback_query(F.data == 'oatmeal_inline4')
@router.callback_query(F.data == 'oatmeal_inline3')
@router.callback_query(F.data == 'oatmeal_inline2')
@router.callback_query(F.data == 'oatmeal_inline1')
async def deserts(call: CallbackQuery):
    """ """
    if call.data == 'oatmeal1' or call.data == 'oatmeal_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='oatmeal2'),
                InlineKeyboardButton(text='➡️', callback_data='oatmeal3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'oatmeal_inline1':
            await call.message.answer(text="<b>ОВСЯНОБЛИН с арахисовой пастой и бананом (КБЖУ: 481/20/20/56)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/Pou1GLei12s?si=7HsqBPAfxYps3Ivu',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>ОВСЯНОБЛИН с арахисовой пастой и бананом (КБЖУ: 481/20/20/56)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/Pou1GLei12s?si=7HsqBPAfxYps3Ivu',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'oatmeal2' or call.data == 'oatmeal_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='oatmeal4'),
                InlineKeyboardButton(text='➡️', callback_data='oatmeal1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'oatmeal_inline2':
            await call.message.answer(text="<b>Овсяная каша в стиле ризотто с яйцом пашот (КБЖУ: 350/26/12/32)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/LFKqbar4Yr4?si=Ffdk53UYIBDRakJ5',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Овсяная каша в стиле ризотто с яйцом пашот (КБЖУ: 350/26/12/32)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/LFKqbar4Yr4?si=Ffdk53UYIBDRakJ5',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'oatmeal3' or call.data == 'oatmeal_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='oatmeal1'),
                InlineKeyboardButton(text='➡️', callback_data='oatmeal5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'oatmeal_inline3':
            await call.message.answer(text="<b>Овсяная каша облачко (КБЖУ: 384/12/8/66)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/6ajEhBg0QeE?si=-4oz8xGtAhqEsX16',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Овсяная каша облачко (КБЖУ: 384/12/8/66)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/6ajEhBg0QeE?si=-4oz8xGtAhqEsX16',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'oatmeal4' or call.data == 'oatmeal_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='oatmeal5'),
                InlineKeyboardButton(text='➡️', callback_data='oatmeal2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'oatmeal_inline4':
            await call.message.answer(text="<b>Имбирный кекс с овсянкой и бананом (КБЖУ: 409/16/12/59)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/T5ZUNhD4AXs?si=W2LhVitGdgJCKgZ-',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Имбирный кекс с овсянкой и бананом (КБЖУ: 409/16/12/59)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/T5ZUNhD4AXs?si=W2LhVitGdgJCKgZ-',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'oatmeal5' or call.data == 'oatmeal_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_oatmeal5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='oatmeal3'),
                InlineKeyboardButton(text='➡️', callback_data='oatmeal4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'oatmeal_inline5':
            await call.message.answer(text="<b>Шокоовсяноблин (КБЖУ: 310/13/11/36)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/17H1ljuAvO4?si=3A7PRC-68iJ2KiRJ',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Шокоовсяноблин (КБЖУ: 310/13/11/36)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/17H1ljuAvO4?si=3A7PRC-68iJ2KiRJ',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_oatmeal5')
@router.callback_query(F.data == 'recipe_oatmeal4')
@router.callback_query(F.data == 'recipe_oatmeal3')
@router.callback_query(F.data == 'recipe_oatmeal2')
@router.callback_query(F.data == 'recipe_oatmeal1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_oatmeal1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='oatmeal_inline1')]
        ])
        await call.message.answer(text="""
                Ингредиенты:
- 1 яйцо
- 60г кокосовое молоко (можно обычное)
- 50г банана (в тесто) 
- 20 г банана (в начинку)
- 20г арахисовая паста
- 50г овсянка ясно солнышко размер №3 
- Разрыхлитель 0,5 ч. л.
- Корица 
- Сахарозаменитель 
- Оливковое масло 1г (смазать сковородку)""",
                                  protect_content=True)
        await call.message.answer(text="""
                Рецепт:
Банан размять вилкой, добавить овсянку, молоко, яйцо, разрыхлитель, корицу и сах.зам.
Выложить на неразогретую сковородку, смазанную немного оливковым маслом. Накрыть крышкой и через 5-7 минут, когда схватится, перевернуть с помощью тарелки или крышки. Еще через 5-7 минут выложить на тарелку, смазать арахисовой пастой и добавить кусочки банана. Свернуть и наслаждаться ☺️""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_oatmeal2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='oatmeal_inline2')]
            ])
            await call.message.answer(text="""
                    Ингредиенты:
Геркулес - 50 гр.
Яйцо куриное С1 - 1 штука
Белок одного яйца - 1 штука
Сыр легкий - 30 гр
Томаты черри
Шампиньона 
Соль, перец, приправа «томаты и чеснок»""",
                                      protect_content=True)
            await call.message.answer(text="""
                    Рецепт:
Геркулес заливаем кипятком, на сковороде тушим помидоры и шампиньоны, добавляем овсянку и белок, солим, добавляем приправы и специи, все перемешиваем, тушим 5-7 минут, сверху трем сыр.

Сверху выкладываем яйцо-пашот (приготовление на видео)""",
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_oatmeal3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='oatmeal_inline3')]
        ])
        await call.message.answer(text="""
                        Ингредиенты:
- Овсянка 45 г
- Белок 1шт 
- Сах.зам и ваниль
- Посластитель в кашу (у меня сироп топинамбура 10 г и банан 50 г)
Наполнение:
- Киндер шоколад палочка
- Банан 20 г
- гранола 12 г""",
                                  protect_content=True)
        await call.message.answer(text="""
                        Приготовить кашу любым удобным способом. Я не люблю вареную кашу, поэтому просто заливаю кипятком обычные хлопья на 10 минут и перемешиваю с бананом и сиропом. 
Взбить белок миксером с сах.замом и ванилью, не до пиков, до состояния плотной пены. 
Добавить белок в кашу, сверху можно добавить шоколад, фрукты, орешки, гранолу, варенье.
UPD: если сомневаетесь в безопасности яиц, то сырой белок можно заменить на пастеризованный белок (продаётся в бутылочках), либо влить белок в горячую кашу и перемешать, получается сливочный вкус.""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_oatmeal4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='oatmeal_inline4')]
            ])
            await call.message.answer(text="""
                        Ингредиенты:
- Банан 50г
- Овсянка 50г
- Яйцо 1шт
- Разрыхлитель 1/2 ч.лож
- Молоко 50г
- Киндер шоколад 1/2 палочки 
- Смесь пряностей, у меня из Вкусвилла, в нее входит: имбирь, корица, бадьян, кардамон, перец душистый, гвоздика, перец черный
- Подсластитель по желанию (я очень люблю послаще, поэтому добавила сахарозаменитель)
""",
                                      protect_content=True)
            await call.message.answer(text="""
                        Рецепт:
В блендере перелемолоть банан, яйцо, овсянку, разрыхлитель, добавить специи. Перелить все в небольшую форму, но не до краев, у меня кекс пытался сбежать. 
Сверху выложить кусочки шоколадки и отправить в духовку на 170С - 20-25мин.

А если добавить сюда еще шарик мороженого или соус из мягкого творожка с ягодами, то будет просто отрыв фонариков 😋""",
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_oatmeal5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='oatmeal_inline5')]
        ])
        await call.message.answer(text="""
                            Ингредиенты:
Овсяные хлопья - 30 гр
Яйцо - 1 шт
Банан - 60 гр
Какао порошок - 5 гр
Молоко 2,5 - 20 мл
Греческий йогурт - 20 г
Подсластитель по вкусу 
По желанию:
Zero сироп молочный шоколад 
Лепестки миндаля 8 г
    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
Смешиваем овсянку, яйцо, какао порошок, молоко и оставляем набухать на 5 мин. 
Можно хлопья помолоть, тогда не надо ждать.
Жарим на разогретой антипригарной сковороде под крышкой только содной стороны, выкладываем начинку: йогурт, банан, любимые топинги, заворчиваем и обжариваем с двух сторон.""",
                                  reply_markup=keyboard,
                                  protect_content=True)