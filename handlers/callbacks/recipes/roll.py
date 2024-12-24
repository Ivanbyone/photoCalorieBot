from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'roll5')
@router.callback_query(F.data == 'roll4')
@router.callback_query(F.data == 'roll3')
@router.callback_query(F.data == 'roll2')
@router.callback_query(F.data == 'roll1')
@router.callback_query(F.data == 'roll_inline5')
@router.callback_query(F.data == 'roll_inline4')
@router.callback_query(F.data == 'roll_inline3')
@router.callback_query(F.data == 'roll_inline2')
@router.callback_query(F.data == 'roll_inline1')
async def rolls(call: CallbackQuery):
    """ """
    if call.data == 'roll1' or call.data == 'roll_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='roll2'),
                InlineKeyboardButton(text='➡️', callback_data='roll3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'roll_inline1':
            await call.message.answer(text="<b> Цезарь ролл (КБЖУ: 429/31/15/41)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/0ib2rlox5fw?si=KM_3BLnnTIgPqeiC',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Цезарь ролл (КБЖУ: 429/31/15/41)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/0ib2rlox5fw?si=KM_3BLnnTIgPqeiC',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'roll2' or call.data == 'roll_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='roll4'),
                InlineKeyboardButton(text='➡️', callback_data='roll1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'roll_inline2':
            await call.message.answer(text="<b>ФИШ РОЛЛ(КБЖУ: 431/20/20/43)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/VItlFJ-temw?si=wkWoBJ1EpHr9b3NO',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>ФИШ РОЛЛ(КБЖУ: 431/20/20/43)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/VItlFJ-temw?si=wkWoBJ1EpHr9b3NO',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'roll3' or call.data == 'roll_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='roll1'),
                InlineKeyboardButton(text='➡️', callback_data='roll5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'roll_inline3':
            await call.message.answer(text="<b>Шримп ролл (КБЖУ: 418/23/16/46)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/oBLaL6Lb4gQ?si=5X-vjRLUFsSJ3foM',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Шримп ролл (КБЖУ: 418/23/16/46)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/oBLaL6Lb4gQ?si=5X-vjRLUFsSJ3foM',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'roll4' or call.data == 'roll_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='roll5'),
                InlineKeyboardButton(text='➡️', callback_data='roll2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'roll_inline4':
            await call.message.answer(text="<b>Шаурма с курицей (КБЖУ: 367/36/10/33)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/SGTo-Au6IGQ?si=MUtDcPIlTRtU_DCg',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Шаурма с курицей (КБЖУ: 367/36/10/33)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/SGTo-Au6IGQ?si=MUtDcPIlTRtU_DCg',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'roll5' or call.data == 'roll_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_roll5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='roll3'),
                InlineKeyboardButton(text='➡️', callback_data='roll4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'roll_inline5':
            await call.message.answer(text="<b>Ролл с яйцом, ветчиной и сыром( КБЖУ: 305/24/11/26)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/9RLKvZi4ZvQ?si=Q882tUKIAkFxbhM1',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Ролл с яйцом, ветчиной и сыром( КБЖУ: 305/24/11/26)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/9RLKvZi4ZvQ?si=Q882tUKIAkFxbhM1',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_roll5')
@router.callback_query(F.data == 'recipe_roll4')
@router.callback_query(F.data == 'recipe_roll3')
@router.callback_query(F.data == 'recipe_roll2')
@router.callback_query(F.data == 'recipe_roll1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_roll1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='roll_inline1')]
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

    if call.data == 'recipe_roll2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='roll_inline2')]
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

    if call.data == 'recipe_roll3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='roll_inline3')]
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

    if call.data == 'recipe_roll4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='roll_inline4')]
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

    if call.data == 'recipe_roll5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='roll_inline5')]
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
