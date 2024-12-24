""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'eggs5')
@router.callback_query(F.data == 'eggs4')
@router.callback_query(F.data == 'eggs3')
@router.callback_query(F.data == 'eggs2')
@router.callback_query(F.data == 'eggs1')
@router.callback_query(F.data == 'eggs_inline5')
@router.callback_query(F.data == 'eggs_inline4')
@router.callback_query(F.data == 'eggs_inline3')
@router.callback_query(F.data == 'eggs_inline2')
@router.callback_query(F.data == 'eggs_inline1')
async def eggss(call: CallbackQuery):
    """ """
    if call.data == 'eggs1' or call.data == 'eggs_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='eggs2'),
                InlineKeyboardButton(text='➡️', callback_data='eggs3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'eggs_inline1':
            await call.message.answer(text="<b> Шакшука (КБЖУ: 417/22/21/34) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/3O3BmiUW8Bg?si=kpBAgyaFNMApMoEj',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Шакшука (КБЖУ: 417/22/21/34)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/3O3BmiUW8Bg?si=kpBAgyaFNMApMoEj',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'eggs2' or call.data == 'eggs_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='eggs4'),
                InlineKeyboardButton(text='➡️', callback_data='eggs1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'eggs_inline2':
            await call.message.answer(text="<b> Омлет в тортилье с сыром и шпинатом (КБЖУ: 290/21,5/13,5/19,5) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                        url='https://youtube.com/shorts/nIqoYrr9KSc?si=K8cl_gTjViMjYlFPl',
                                        prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Омлет в тортилье с сыром и шпинатом (КБЖУ: 290/21,5/13,5/19,5) </b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/nIqoYrr9KSc?si=K8cl_gTjViMjYlFPl',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'eggs3' or call.data == 'eggs_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='eggs1'),
                InlineKeyboardButton(text='➡️', callback_data='eggs5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'eggs_inline3':
            await call.message.answer(text="<b> Яйцо в авокадо (КБЖУ: 304/16/26/4)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/dCerGQOhtxA?si=bk4VJcYnyC6Jkpd',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Яйцо в авокадо (КБЖУ: 304/16/26/4)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/dCerGQOhtxA?si=bk4VJcYnyC6Jkpd_',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'eggs4' or call.data == 'eggs_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='eggs5'),
                InlineKeyboardButton(text='➡️', callback_data='eggs2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'eggs_inline4':
            await call.message.answer(text="<b> Яйца в тосте с ветчиной и сыром (КБЖУ: 308/20/14/22)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/guNAxfyshpI?si=3KhGcGpZDy4zg8y7',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Яйца в тосте с ветчиной и сыром (КБЖУ: 308/20/14/22)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/guNAxfyshpI?si=3KhGcGpZDy4zg8y7',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'eggs5' or call.data == 'eggs_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_eggs5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='eggs3'),
                InlineKeyboardButton(text='➡️', callback_data='eggs4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'eggs_inline5':
            await call.message.answer(text="<b> Тортилья с яйцом и сыром/ветчиной (КБЖУ: 350/17/21/21) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/dpWAWahBFBw?si=c7dXze0srfNJPr2v',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Тортилья с яйцом и сыром/ветчиной (КБЖУ: 350/17/21/21)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/dpWAWahBFBw?si=c7dXze0srfNJPr2v',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_eggs5')
@router.callback_query(F.data == 'recipe_eggs4')
@router.callback_query(F.data == 'recipe_eggs3')
@router.callback_query(F.data == 'recipe_eggs2')
@router.callback_query(F.data == 'recipe_eggs1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_eggs1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='eggs_inline1')]
        ])
        await call.message.answer(text=""" 
               Ингредиенты: 
На две порции:
- 1 чл л масла 
- 1 луковица
- 3 зубчика чеснока
- 2 помидора
- 1 столовая ложка томатного соуса (у меня болоньезе, вкуснее обычной томатной пасты)
- ⅓ чайной ложки молотой куркумы
- 1 ч. л. копченой паприки 
- 4 крупных яйца
- Соль, перец 
+
- хлеб 50 гр на одну порцию

""",
                                  protect_content=True)
        await call.message.answer(text="""
                Приготовление:
1. Разогреть масло в большой сковороде, добавить нарезанный лук, обжарить в течение 5 минут, часто помешивая, затем добавить чеснок, готовить около 1 минуты или до появления аромата. 
2. Добавить натертые помидоры, томатное пюре (пасту) и 4 столовые ложки воды, приправить солью и перцем, добавить приправы и 150 мл воды. Довести до кипения, уменьшить огонь до минимума и тушить, пока соус не станет густым.
3. Сделать в соусе 4 углубления. Разбить яйца прямо на сковороду. Накрыть крышкой на 5-10 минут. 
4. Подавать с горячим хлебушком прямо со сковороды 😋



""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_eggs2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='eggs_inline2')]
            ])
            await call.message.answer(text="""
		Ингредиенты: 
КБЖУ на одну порцию: 290/21,5/13,5/19,5
КБЖУ на всё блюдо: 581/43/27/39

- Тортилья большая - 65 гр.
- Яйцо куриное С1 - 3 штуки 
- Творожное зерно в сливках - 100 гр
- Сыр легкий - 15 гр
- Томаты черри
- Шпинат
- Соль, перец, приправы


""",
                                      protect_content=True)
            await call.message.answer(text="""
Приготовление: 

1. Тортилью выкладываем в форму 
2. Туда разбиваем три яйца, выкладываем творожное зерно, соль, приправы
3. Все перемешиваем 
4. Добавляем помидоры и шпинат и сыр 
5. Убираем в духовку на 10-15 минут при 180’ 
6. Достаем и наслаждаемся ❤


 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_eggs3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='eggs_inline3')]
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
4. Можно есть ложкой прямо из авокадо и наслаждаться 🥑 

""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_eggs4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='eggs_inline4')]
            ])
            await call.message.answer(text="""
         Ингредиенты:

- хлеб тостовый Геркулес 40 г 
- арахисовая паста 8 г (можно шоколадную или вообще кусочек шоколадки) 
- яйцо с1 
- Помидор кружочек 
- ветчина из индейки 30 г 
- сыр легкий 15 г 
- соль, перец по вкусу
""",
                                      protect_content=True)
            await call.message.answer(text="""
		Приготовление:

- Вырежите кружочки из хлеба стаканом 
- На круглые части положите арахисовую пасту или шоколад и обжарьте на свороде/гриле с двух сторон 
- На антипригарную сковородку/гриль выложите хлеб, разбейте яйцо в отверстие, готовьте до готовности яйца 
- В другой кусочек хлеба положите помидор, ветчину и сыр 
- Накройте одну половинку хлеба другой половинкой и наслаждайтесь ❤️


 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_eggs5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='eggs_inline5')]
        ])
        await call.message.answer(text="""
  	Ингредиенты:
- Тортилья Mission Deli - 39 гр
- Сыр творожный - 10 гр
- Яйцо куриное - 54 гр
- Помидор - 30 гр
- Ветчина Индилайт - 40 гр
- Соус ореховый - 5 гр

    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:

1. Смазать тортилью творожным сыром.
2. Взбить яйцо вилкой, вылить на разогретую сковородку, накрыть крышкой на 1 – 2 минуты.
3. Прижать сверху тортилью, чтобы яйцо схватилось, перевернуть 
4. Выложить сверху помидор, добавить сыр, ветчину и готовить под крышкой до готовности.
""",
                                  reply_markup=keyboard,
                                  protect_content=True)
