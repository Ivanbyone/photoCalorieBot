''' '''

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'desert5')
@router.callback_query(F.data == 'desert4')
@router.callback_query(F.data == 'desert3')
@router.callback_query(F.data == 'desert2')
@router.callback_query(F.data == 'desert1')
@router.callback_query(F.data == 'desert_inline5')
@router.callback_query(F.data == 'desert_inline4')
@router.callback_query(F.data == 'desert_inline3')
@router.callback_query(F.data == 'desert_inline2')
@router.callback_query(F.data == 'desert_inline1')
async def deserts(call: CallbackQuery):
    """ """
    if call.data == 'desert1' or call.data == 'desert_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='desert2'),
                InlineKeyboardButton(text='➡️', callback_data='desert3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'desert_inline1':
            await call.message.answer(text="<b> Запеченные груши с творогом и рикоттой (КБЖУ: 383/24/12/28)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/YD18NMtn_v8?si=GuPBb-zWIUwMpHP7',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Запеченные груши с творогом и рикоттой (КБЖУ: 383/24/12/28)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/YD18NMtn_v8?si=GuPBb-zWIUwMpHP7',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'desert2' or call.data == 'desert_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='desert4'),
                InlineKeyboardButton(text='➡️', callback_data='desert1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'desert_inline2':
            await call.message.answer(text="<b>Чизкейк (КБЖУ на весь: 604/30/36/30)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/inAPf1DMIEc?si=mTV0vDTd-6LPZBfR',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Чизкейк (КБЖУ на весь: 604/30/36/30)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/inAPf1DMIEc?si=mTV0vDTd-6LPZBfR',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'desert3' or call.data == 'desert_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='desert1'),
                InlineKeyboardButton(text='➡️', callback_data='desert5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'desert_inline3':
            await call.message.answer(text="<b>Протеиновые вафли с маршмеллоу (КБЖУ: 381/29/9/43)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/oBDTFVklOlc?si=FF99k49t2PnnA-5C',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Протеиновые вафли с маршмеллоу (КБЖУ: 381/29/9/43)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/oBDTFVklOlc?si=FF99k49t2PnnA-5C',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'desert4' or call.data == 'desert_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='desert5'),
                InlineKeyboardButton(text='➡️', callback_data='desert2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'desert_inline4':
            await call.message.answer(text="<b>Пухлик (КБЖУ: 277/17/9/28)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/1R14-Y2sP2Y?si=XIQazVTVhqN_hkLn',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Пухлик (КБЖУ: 277/17/9/28)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/1R14-Y2sP2Y?si=XIQazVTVhqN_hkLn',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'desert5' or call.data == 'desert_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_desert5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='desert3'),
                InlineKeyboardButton(text='➡️', callback_data='desert4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'desert_inline5':
            await call.message.answer(text="<b>Шарлотка (КБЖУ 1/6 части: 89/5/1/15)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/hoftVfnmJVw?si=-_b9xIRUo5B0sXd8',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Шарлотка (КБЖУ 1/6 части: 89/5/1/15)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/hoftVfnmJVw?si=-_b9xIRUo5B0sXd8',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_desert5')
@router.callback_query(F.data == 'recipe_desert4')
@router.callback_query(F.data == 'recipe_desert3')
@router.callback_query(F.data == 'recipe_desert2')
@router.callback_query(F.data == 'recipe_desert1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_desert1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='desert_inline1')]
        ])
        await call.message.answer(text=""" 
Ингредиенты: 
- творог в брикете 0-2% 80 г 
- рикотта лайт (у меня ВкусВилл) 80 г 
- груша 2 штуки 
- сироп топинамбура 15 г 
- грецкий орех 5 г 
- сахарозаменитель (фит парад) """,
                                  protect_content=True)
        await call.message.answer(text="""
                Рецепт:
Груши разрезаем пополам, вырезаем центральную часть, чтобы было побольше места для начинки. Смешиваем рикотту, творог, сироп и сах.зам. Хорошо перемешиваем, выкладываем в груши, сверху можно посыпать грецким/кедровым орехом. Убираем в разогретую до 180 градусов духовку на 20 минут. Вынимаем, украшаем, можно добавить холодный йогурт с ягодами 🔥
""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_desert2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='desert_inline2')]
            ])
            await call.message.answer(text="""
                    Ингредиенты:
- Творожный сыр (у меня альметте, можно найти более легкий вариант) 130 г 
- Мягкий творог Савушкин 0,1% 150 г
- Яйцо с1
- Кукурузный крахмал 2 ст л ≈ 30 г
- Сахарозаменитель или подсластитель по вкусу (2 пакетика фит. парад)
- Ванилин
""",
                                      protect_content=True)
            await call.message.answer(text="""
                    Рецепт:
Смешиваем все ингредиенты и отправляем в микроволновку на 5 минут. Сверху можно украсить йогуртом и ягодами. Можно есть сразу, но тогда по вкусу это больше запеканка. А если дать ему постоять пару часов, то получится чизкейк не хуже чем в магазине. 
 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_desert3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='desert_inline3')]
        ])
        await call.message.answer(text="""
                        Ингредиенты:
- Пудинг Ehrmann High Protein высокобелковый - 200 г
- 1 яйцо 
- Мука рисовая 30 г
- Маршмеллоу 10 г

""",
                                  protect_content=True)
        await call.message.answer(text="""
Перемешать пудинг с яйцом и мукой, выложить в силиконовую форму (у меня из FixPrice), выпекать 7 минут в разогретой до 180 градусов духовке, либо в вафельнице, смазанной маслом, но есть риск, что они прилипнут. На одну половинку вафли выложить маршмеллоу и накрыть второй половинкой. Наслаждаться 😋
                        """,
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_desert4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='desert_inline4')]
            ])
            await call.message.answer(text="""
Ингредиенты: 
- 4 хлебца (у меня гречневые Dr.Korner , но можно любые) 
- Яблоко 50гр (можно грушу или любой другой фрукт или ягоды) 
- 1 яйцо 
- 1 белок
- Корица (много 😋), сах зам

""",
                                      protect_content=True)
            await call.message.answer(text="""
                        Рецепт:
1. Ставим разогреваться духовку на 220 градусов
2. Крошим хлебцы (лучше крупными кусочками) 
3. Добавляем яблоко, яйцо, белок, корицу и сах. зам.
4. Все хорошенько перемешиваем 
5. Отправляем в духовку на 15 минут.
6. Сверху поливаем любимым топпингом (у меня арахисовая паста)
 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_desert5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='desert_inline5')]
        ])
        await call.message.answer(text="""
  		Ингредиенты на 6 порций:

- 150 г яичных белков (у меня в картонной упаковке от Вкусвилла)
- 1 яйцо
- 60гр муки (у меня рисовая )
- 350 г яблок 
- подсластитель (у меня фит.парад)
- Смесь специй (ваниль, корица)
- щепотка соли по вкусу
    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:

1. Взбить все белки до крепких пиков
2. Добавить муку, сахарозаменитель, специи и желток
3. Очень аккуратно перемешать лопаткой
4. Нарезать яблоки на кубики
5. Выложить в форму порезанные яблоки. (У меня силиконовая форма, к ней ничего не прилипает, если форма алюминиевая, то стоит еще смазать маслом)
6. Отправить в разогретую до 180гр. духовку на 30 - 40 минут 
Можно кушать теплой с шариком мороженого, можно остывшей. В любом случае будет очень вкусно.
""",
                                  reply_markup=keyboard,
                                  protect_content=True)



@router.callback_query(F.data == "recipe_deserts1")
@router.callback_query(F.data == 'recipe_deserts2')
async def recipe_deserts(call: CallbackQuery):
    """ """
    if call.data == "recipe_deserts1":

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='deserts2')]
        ])

        await call.message.answer(text="""
        ИНГРЕДИЕНТЫ\n
20–30 г сливочного масла
2 больших банана
50 г коричневого сахара
семена половины стручка ванили
400 мл натурального йогурта
грецкие орехи и ягоды для украшения""")
        await call.message.answer(text="""
        ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ

- Шаг 1

В сковороде растопите сливочное масло. Положите бананы, нарезанные кусочками, коричневый сахар и семена ванили. Готовьте на среднем огне 2–3 мин., помешивая.

- Шаг 2

В стаканы для виски положите по 2 ст. л. натурального йогурта, потом – половину бананов, йогурт, оставшиеся бананы, йогурт. Сверху посыпьте измельченными грецкими орехами и украсьте свежими ягодами.

Приятного аппетита😋""",
                                  reply_markup=keyboard)

    elif call.data == "recipe_deserts2":

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='deserts2')]
        ])

        await call.message.answer(text="""
        ИНГРЕДИЕНТЫ\n
200 г мороженого с карамелью
200 г пломбира
200 г густой карамели или вареной сгущенки
40 г соленого арахиса
3 ст. л. домашней арахисовой пасты
2 ст. л. молока
2 банана
100 г вкусных вафель со сгущенкой или шоколадной начинкой
морская соль""")

        await call.message.answer(text="""
        ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ

- Шаг 1

приготовление соуса
Прогрейте в сотейнике, аккуратно перемешивая, карамель, арахисовую пасту, молоко и щепотку соли. Должна получиться однородная масса.

- Шаг 2

раскладывание соуса
Распределите половину соуса по 4 высоким бокалам или креманкам.

- Шаг 3

раскладывание пломбира
Добавьте по 1 шарику мороженого и 1 шарику пломбира плюс кусочки банана.

- Шаг 4

украшение десерта
Разлейте оставшийся соус и посыпьте мелко нарезанными орехами. Украсьте кусочками вафель. Сразу подавайте.

Приятного аппетита😋""",
                                  reply_markup=keyboard)
