from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'avocado5')
@router.callback_query(F.data == 'avocado4')
@router.callback_query(F.data == 'avocado3')
@router.callback_query(F.data == 'avocado2')
@router.callback_query(F.data == 'avocado1')
@router.callback_query(F.data == 'avocado_inline5')
@router.callback_query(F.data == 'avocado_inline4')
@router.callback_query(F.data == 'avocado_inline3')
@router.callback_query(F.data == 'avocado_inline2')
@router.callback_query(F.data == 'avocado_inline1')
async def avocados(call: CallbackQuery):
    """ """
    if call.data == 'avocado1' or call.data == 'avocado_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='avocado2'),
                InlineKeyboardButton(text='➡️', callback_data='avocado3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'avocado_inline1':
            await call.message.answer(text="<b>Сэндвич с авокадо ( КБЖУ: 417/20/27/27)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/Pg5HGQDrM4w?si=xvuYVbTG_KBO08Ug',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Сэндвич с авокадо ( КБЖУ: 417/20/27/27)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/Pg5HGQDrM4w?si=xvuYVbTG_KBO08Ug',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'avocado2' or call.data == 'avocado_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='avocado4'),
                InlineKeyboardButton(text='➡️', callback_data='avocado1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'avocado_inline2':
            await call.message.answer(text="<b>Намазка из тунца и авокадо (КБЖУ: 420/28/21/28)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/Eg5A4xBfNC8?si=CZyiEait7XKwNZkr',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Намазка из тунца и авокадо (КБЖУ: 420/28/21/28)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/Eg5A4xBfNC8?si=CZyiEait7XKwNZkr',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'avocado3' or call.data == 'avocado_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='avocado1'),
                InlineKeyboardButton(text='➡️', callback_data='avocado5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'avocado_inline3':
            await call.message.answer(text="<b> Яйцо в авокадо (КБЖУ: 304/16/26/4) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/dCerGQOhtxA?si=bk4VJcYnyC6Jkpd_',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Яйцо в авокадо (КБЖУ: 304/16/26/4)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/dCerGQOhtxA?si=bk4VJcYnyC6Jkpd_',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'avocado4' or call.data == 'avocado_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='avocado5'),
                InlineKeyboardButton(text='➡️', callback_data='avocado2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'avocado_inline4':
            await call.message.answer(text="<b>Суши-сэндвич (КБЖУ:260/17/10/24)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/uOtlgvkEWnU?si=XCQtV8E288Y1dVKV',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Суши-сэндвич (КБЖУ:260/17/10/24)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/uOtlgvkEWnU?si=XCQtV8E288Y1dVKV',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'avocado5' or call.data == 'avocado_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_avocado5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='avocado3'),
                InlineKeyboardButton(text='➡️', callback_data='avocado4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'avocado_inline5':
            await call.message.answer(text="<b>Паста с авокадо и тунцом (КБЖУ: 374/26/12/39)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/ldHdIHY-Yl8?si=zC8VuNA7hIw4Z3Nl',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Паста с авокадо и тунцом (КБЖУ: 374/26/12/39)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/ldHdIHY-Yl8?si=zC8VuNA7hIw4Z3Nl',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_avocado5')
@router.callback_query(F.data == 'recipe_avocado4')
@router.callback_query(F.data == 'recipe_avocado3')
@router.callback_query(F.data == 'recipe_avocado2')
@router.callback_query(F.data == 'recipe_avocado1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_avocado1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='avocado_inline1')]
        ])
        await call.message.answer(text=""" 
               Ингредиенты: 
- спелое авокадо 80 г
(Важно, чтобы оно было спелое и мягкое)
- форель слабосоленая 70 г
- хлеб тостовый 50 г
- сыр творожный 10 г
""",
                                  protect_content=True)
        await call.message.answer(text="""
                Приготовление: 
Нарезать авокадо, рыбу, хлеб поджарить в тостере/на гриле. Смазать творожным сыром, выложить слой авокадо, потом слой рыбки и так сколько хватит терпения и ингредиентов. Накрыть вторым кусочком хлеба, разрезать напополам и наслаждаться 🙌🏼
""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_avocado2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='avocado_inline2')]
            ])
            await call.message.answer(text="""
		Ингредиенты: 
- спелое авокадо 80 г
- яйцо с1
- тунец консервированный 70 г
- творожный сыр 15 г
- хлеб тостовый Геркулес 40 г
- соль, перец по вкусу ⠀
""",
                                      protect_content=True)
            await call.message.answer(text="""
Приготовление: 
1. Авокадо почистить, размять вилкой 
2. Яйцо отварить, размять вилкой и добавить к авокадо 
3. Добавить тунец, размять все в однородную массу 
4. Добавить соль, специи, лимонный сок 
5. Хлеб поджарить в тостере, намазать сверху намазку.⠀
 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_avocado3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='avocado_inline3')]
        ])
        await call.message.answer(text="""
		Ингредиенты: 
- спелое авокадо 90 г
- яйцо с1 (54 г)
- Моцарелла мини 15 г
- йогурт греческий 15 г
- сыр легкий 15 г
- соль, перец по вкусу
     """,
                                  protect_content=True)
        await call.message.answer(text="""
Приготовление:
1. Разрезать авокадо вдоль на 2 части, удалить косточки и аккуратно ложкой вытащить часть мякоти, чтобы увеличить углубление
2. Уложить в углубление сыр, йогурт и аккуратно влить сверху яйцо (я делила на два авокадо одно яйцо)
3. Поставить в духовку, разогретую до 180 градусов на 15-20 минут (смотря какой желток хотите)
4. Можно есть ложкой прямо из авокадо и наслаждаться ❤
                        """,
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_avocado4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='avocado_inline4')]
            ])
            await call.message.answer(text="""
         Ингредиенты:

- рис ≈ 25 гр в сухом виде (у меня 1/4 пакетика)
- Сыр творожный 10 гр
- Авокадо 25 гр (половина половинки)
- Нори лист ≈ 5 гр
- Креветки 40 гр
- Семга слабосоленая 30 гр
""",
                                      protect_content=True)
            await call.message.answer(text="""
		Приготовление:

1. Рис отварить в пакетиках, креветки залить кипятком или тоже отварить с рисом. 
2. Разрезать нори, выложить рис, сверху сыр, креветки, размятый авокадо, рыбку.

Внимание!!! Не смазывайте саму нори творожным сыром, она от этого превращается в кашу.
 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_avocado5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='avocado_inline5')]
        ])
        await call.message.answer(text="""
  	Ингредиенты:
- авокадо хаас 50 г
- тунец консервированный в собственном соку 75 г
- творожный сыр 15 г
- паста барилла 50 г
- соль, специи, сок лимона, овощи по вкусу ❤

    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
1. Размять авокадо с творожным сыром, 
2. Добавить тунец
3. Добавить специи и всё хорошо перемешать 
4. Отварить макароны и добавить к тунцу, перемешать и наслаждаться ❤
Это очень вкусно, а главное быстро готовится, обязательно попробуйте!

""",
                                  reply_markup=keyboard,
                                  protect_content=True)
