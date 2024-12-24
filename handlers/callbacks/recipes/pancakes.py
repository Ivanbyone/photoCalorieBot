from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'pancakes5')
@router.callback_query(F.data == 'pancakes4')
@router.callback_query(F.data == 'pancakes3')
@router.callback_query(F.data == 'pancakes2')
@router.callback_query(F.data == 'pancakes1')
@router.callback_query(F.data == 'pancakes_inline5')
@router.callback_query(F.data == 'pancakes_inline4')
@router.callback_query(F.data == 'pancakes_inline3')
@router.callback_query(F.data == 'pancakes_inline2')
@router.callback_query(F.data == 'pancakes_inline1')
async def pancakess(call: CallbackQuery):
    """ """
    if call.data == 'pancakes1' or call.data == 'pancakes_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='pancakes2'),
                InlineKeyboardButton(text='➡️', callback_data='pancakes3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'pancakes_inline1':
            await call.message.answer(text="<b>Творожные оладьи с луком и сыром (КБЖУ: 352/26/15/25)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/fPugTMZVZ0k?si=KMR24MA6sE5xTl_u',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Творожные оладьи с луком и сыром (КБЖУ: 352/26/15/25)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/fPugTMZVZ0k?si=KMR24MA6sE5xTl_u',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'pancakes2' or call.data == 'pancakes_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='pancakes4'),
                InlineKeyboardButton(text='➡️', callback_data='pancakes1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'pancakes_inline2':
            await call.message.answer(text="<b>Банановые панкейки с шоколадом и мягким творогом (КБЖУ: 521/25/18/65)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/GHCjZeKwYRs?si=J5rHPTDUBNm3xzv8',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Банановые панкейки с шоколадом и мягким творогом (КБЖУ: 521/25/18/65)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/GHCjZeKwYRs?si=J5rHPTDUBNm3xzv8',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'pancakes3' or call.data == 'pancakes_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='pancakes1'),
                InlineKeyboardButton(text='➡️', callback_data='pancakes5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'pancakes_inline3':
            await call.message.answer(text="<b>Драники из кабачка (КБЖУ: 244/12/6/35)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/VYMfSAflj2k?si=RNGxiWN-fGUKMBJq',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Драники из кабачка (КБЖУ: 244/12/6/35)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/VYMfSAflj2k?si=RNGxiWN-fGUKMBJq',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'pancakes4' or call.data == 'pancakes_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='pancakes5'),
                InlineKeyboardButton(text='➡️', callback_data='pancakes2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'pancakes_inline4':
            await call.message.answer(text="<b>Вафли с тунцом и сыром (КБЖУ: 454/42/11/43)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/-uiVNJkPZj0?si=5a1v_bemW4-drtzk',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Вафли с тунцом и сыром (КБЖУ: 454/42/11/43)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/-uiVNJkPZj0?si=5a1v_bemW4-drtzk',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'pancakes5' or call.data == 'pancakes_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_pancakes5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='pancakes3'),
                InlineKeyboardButton(text='➡️', callback_data='pancakes4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'pancakes_inline5':
            await call.message.answer(text="<b>Сырные вафли (КБЖУ: 361/25/13/33)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/FIChAsORsYk?si=Saa6Okfji9D4xMxq',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Сырные вафли (КБЖУ: 361/25/13/33)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/FIChAsORsYk?si=Saa6Okfji9D4xMxq',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_pancakes5')
@router.callback_query(F.data == 'recipe_pancakes4')
@router.callback_query(F.data == 'recipe_pancakes3')
@router.callback_query(F.data == 'recipe_pancakes2')
@router.callback_query(F.data == 'recipe_pancakes1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_pancakes1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pancakes_inline1')]
        ])
        await call.message.answer(text=""" 
               Ингредиенты: 
- мягкий творог 5% 120 г
- мука 30 г
- зеленый лук 30 г 
- яйцо С1
- сыр адыгейский 25 г
- Соль, перец по вкусу
""",
                                  protect_content=True)
        await call.message.answer(text="""
                Приготовление: 
1. Смешиваем творог, яйцо, муку, сыр и лук;
2. Выпекаем оладьи на сковороде;
3. Подаем с греческим йогуртом.
""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_pancakes2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='pancakes_inline2')]
            ])
            await call.message.answer(text="""
		Ингредиенты: 
- банан 80 г
- яйцо куриное
- мука (любая) 30 гр
- сахзам по желанию
- варенье/соус - 35 г
- растительное масло 1 ч.л.
- мягкий творог 4% 150 гр
- ягоды замороженные 40 гр
- сироп топинамбура/zero/сахзам⠀
""",
                                      protect_content=True)
            await call.message.answer(text="""
Приготовление: 

1. Банан измельчить в блендере или размять вилкой до однородной массы
2. Добавить яйцо, сах. зам, хорошо перемешать
3. Постепенно вмешать муку
4. Обжарить с двух сторон на 1 ч.л. масла
5. Мягкий творог смешать с подсластителем и ягодами
 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_pancakes3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pancakes_inline3')]
        ])
        await call.message.answer(text="""
		Ингредиенты: 
- Кабачок/капуста 300 гр, 
- 1 яйцо с1,
- Мука пшеничная/ рисовая 30 гр,
- соль, специи по вкусу
     """,
                                  protect_content=True)
        await call.message.answer(text="""
Приготовление: 
1. Кабачок помыть, отрезать попки и натереть на мелкой терке, отжать хорошенько руками, слить жидкость.
2. Добавить яйцо, муку, соль, перец, хорошенько перемешать.
3. Жарить с двух сторон на медленном огне. 
4. Выложить на тарелку, можно дополнительно добавить йогурт, белок (креветки, лосось)
P.S. по такому же принципу можно приготовить драники из тыквы, картошки, батата, яблока и т.д ❤
                        """,
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_pancakes4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='pancakes_inline4')]
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

    if call.data == 'recipe_pancakes5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pancakes_inline5')]
        ])
        await call.message.answer(text="""
  	Ингредиенты:
- сыр легкий 30% - 40 г 
- яйцо С1 
- мука рисовая - 40 г 
- молоко 2,5% - 40 мл 
- мягкий творог 0,1% - 30 г
- разрыхлитель 1/2 чл
- Соль, перец по вкусу 
P.S. Можно добавить еще яйцо сверху по желанию, необходимо учесть это в итоговой калорийности

    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
1. Сыр натереть, смешать все ингредиенты 
2. Вылить на раскаленную вафельницу, жарить 7-10 минут

""",
                                  reply_markup=keyboard,
                                  protect_content=True)
