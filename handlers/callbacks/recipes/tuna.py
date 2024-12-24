from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'tuna5')
@router.callback_query(F.data == 'tuna4')
@router.callback_query(F.data == 'tuna3')
@router.callback_query(F.data == 'tuna2')
@router.callback_query(F.data == 'tuna1')
@router.callback_query(F.data == 'tuna_inline5')
@router.callback_query(F.data == 'tuna_inline4')
@router.callback_query(F.data == 'tuna_inline3')
@router.callback_query(F.data == 'tuna_inline2')
@router.callback_query(F.data == 'tuna_inline1')
async def tunas(call: CallbackQuery):
    """ """
    if call.data == 'tuna1' or call.data == 'tuna_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='tuna2'),
                InlineKeyboardButton(text='➡️', callback_data='tuna3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'tuna_inline1':
            await call.message.answer(text="<b> ПОКЕ с рисом, тунцом и креветками (КБЖУ: 449/20/14/56) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/bF4_J4Y4oBY?si=mrQmEhjVxVF9hpak',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> ПОКЕ с рисом, тунцом и креветками (КБЖУ: 449/20/14/56)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/bF4_J4Y4oBY?si=mrQmEhjVxVF9hpak',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'tuna2' or call.data == 'tuna_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='tuna4'),
                InlineKeyboardButton(text='➡️', callback_data='tuna1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'tuna_inline2':
            await call.message.answer(text="<b> Паста с авокадо и тунцом (КБЖУ: 374/26/12/39)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/ldHdIHY-Yl8?si=zC8VuNA7hIw4Z3Nl',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Паста с авокадо и тунцом (КБЖУ: 374/26/12/39) </b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/ldHdIHY-Yl8?si=zC8VuNA7hIw4Z3Nl',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'tuna3' or call.data == 'tuna_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='tuna1'),
                InlineKeyboardButton(text='➡️', callback_data='tuna5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'tuna_inline3':
            await call.message.answer(text="<b> Намазка из тунца и авокадо (КБЖУ: 420/28/21/28) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/Eg5A4xBfNC8?si=CZyiEait7XKwNZkr',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Намазка из тунца и авокадо (КБЖУ: 420/28/21/28)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/Eg5A4xBfNC8?si=CZyiEait7XKwNZkr',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'tuna4' or call.data == 'tuna_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='tuna5'),
                InlineKeyboardButton(text='➡️', callback_data='tuna2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'tuna_inline4':
            await call.message.answer(text="<b> Вафли с тунцом и сыром (КБЖУ: 454/42/11/43) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/-uiVNJkPZj0?si=5a1v_bemW4-drtzk',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Вафли с тунцом и сыром (КБЖУ: 454/42/11/43)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/-uiVNJkPZj0?si=5a1v_bemW4-drtzk',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'tuna5' or call.data == 'tuna_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_tuna5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='tuna3'),
                InlineKeyboardButton(text='➡️', callback_data='tuna4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'tuna_inline5':
            await call.message.answer(text="<b> Ролл с тунцом (КБЖУ: 345/25/10/38) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/0F0kNvjAQYA?si=e9zN9IqssoKnEJWa',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Ролл с тунцом (КБЖУ: 345/25/10/38)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/0F0kNvjAQYA?si=e9zN9IqssoKnEJWa',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_tuna5')
@router.callback_query(F.data == 'recipe_tuna4')
@router.callback_query(F.data == 'recipe_tuna3')
@router.callback_query(F.data == 'recipe_tuna2')
@router.callback_query(F.data == 'recipe_tuna1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_tuna1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='tuna_inline1')]
        ])
        await call.message.answer(text=""" 
               Ингредиенты: 
- рис 40 гр в сухом виде или 120 гр в готовом (в рис добавляю чайную ложку уксуса для риса)
- Тунец 80 гр
- Креветки/мидии 20 гр 
- Манго 50 гр
- Авокадо 25 грамм
- Огурец 🥒 
- Чукка в ореховом соусе 30 гр
- Соус Ореховый Tamaki - 20 гр

""",
                                  protect_content=True)
        await call.message.answer(text="""
                Приготовление:
1. Креветки отварить в кипящей подсоленной воде 3 минуты. 
2. Рис отварить до готовности (я беру в пакетиках и варю в кипящей подсоленной воде 25 минут)
3. Манго, авокадо порезать кубиками, огурец -соломкой.
4. Соединить все ингредиенты в глубокой тарелке секторами, полить соусами.
5. Сверху порезать стружкой нори или посыпать кунжутом


""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_tuna2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='tuna_inline2')]
            ])
            await call.message.answer(text="""
		Ингредиенты: 
- авокадо хаас 50 г
- тунец консервированный в собственном соку 75 г
- творожный сыр 15 г
- паста барилла 50 г
- соль, специи, сок лимона, овощи по вкусу ❤️

""",
                                      protect_content=True)
            await call.message.answer(text="""
Приготовление: 

1. Размять авокадо с творожным сыром, 
2. Добавить тунец
3. Добавить специи и всё хорошо перемешать 
4. Отварить макароны и добавить к тунцу, перемешать и наслаждаться ❤
Это очень вкусно, а главное быстро готовится, обязательно попробуйте!


 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_tuna3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='tuna_inline3')]
        ])
        await call.message.answer(text="""
		Ингредиенты: 
- спелое авокадо 80 г
- яйцо с1
- тунец консервированный 70 г
- творожный сыр 15 г
- хлеб тостовый Геркулес 40 г
- соль, перец по вкусу
     """,
                                  protect_content=True)
        await call.message.answer(text="""
Приготовление: 
1. Авокадо почистить, размять вилкой 
2. Яйцо отварить, размять вилкой и добавить к авокадо 
3. Добавить тунец, размять все в однородную массу 
4. Добавить соль, специи, лимонный сок 
5. Хлеб поджарить в тостере, намазать сверху намазку.""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_tuna4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='tuna_inline4')]
            ])
            await call.message.answer(text="""
         Ингредиенты:
- 1 яйцо
- 100г нежирного йогурта
- 80г тунца (консервированного в воде) 
- 60г муки
- 20г сыра 
- Укроп
- Соль
""",
                                      protect_content=True)
            await call.message.answer(text="""
		Приготовление:
1. Смешать йогурт, яйцо и муку. 
2. Добавить тунец, сыр, зелень и соль по вкусу. 
3. Все хорошенько перемешать и выпекать до хрустящей корочки.


 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_tuna5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='tuna_inline5')]
        ])
        await call.message.answer(text="""
  	Ингредиенты:
- Тортилья большая - 65 гр.
- Тунец консервированный в собственном соку - 80 гр.
- Сыр творожный/ сметана - 30 г
- Красный лук 1/2
- Соль,черный перец
- Огурец
- помидор
- Салат
+ дополнительно можно использовать соус ZERO чесночный

    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
1. Тунец размять вилкой, добавить туда порезанный огурец, лук, соль, перец, творожный сыр или сметану.
2. На тортилью выложить салатный лист, тунец, огурец, помидор 
3. Свернуть в ролл и обжарить на гриле без масла.

""",
                                  reply_markup=keyboard,
                                  protect_content=True)
