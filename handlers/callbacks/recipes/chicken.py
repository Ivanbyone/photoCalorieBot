""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'chicken7')
@router.callback_query(F.data == 'chicken6')
@router.callback_query(F.data == 'chicken5')
@router.callback_query(F.data == 'chicken4')
@router.callback_query(F.data == 'chicken3')
@router.callback_query(F.data == 'chicken2')
@router.callback_query(F.data == 'chicken1')
@router.callback_query(F.data == 'chicken7_inline')
@router.callback_query(F.data == 'chicken6_inline')
@router.callback_query(F.data == 'chicken5_inline')
@router.callback_query(F.data == 'chicken4_inline')
@router.callback_query(F.data == 'chicken3_inline')
@router.callback_query(F.data == 'chicken2_inline')
@router.callback_query(F.data == 'chicken1_inline')
async def deserts(call: CallbackQuery):
    """ """
    if call.data == 'chicken1' or call.data == 'chicken1_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken2'),
                InlineKeyboardButton(text='➡️', callback_data='chicken3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken1_inline':
            await call.message.answer(text="<b>Хрустящая курица в панировке (2 порции) (КБЖУ: 322/56/6/5)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/7dny6Sww9a8?si=tYyIDI-o4QWO6z6W',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Хрустящая курица в панировке (2 порции) (КБЖУ: 322/56/6/5)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/7dny6Sww9a8?si=tYyIDI-o4QWO6z6W',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
    if call.data == 'chicken2' or call.data == 'chicken2_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken4'),
                InlineKeyboardButton(text='➡️', callback_data='chicken1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken2_inline':
            await call.message.answer(text="<b>Цезарь с курицей (КБЖУ: 317/39/14/6)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/Ji3vWJ184Nk?si=sbd0HxHQFSqlmfYl',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Цезарь с курицей (КБЖУ: 317/39/14/6)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/Ji3vWJ184Nk?si=sbd0HxHQFSqlmfYl',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )

    if call.data == 'chicken3' or call.data == 'chicken3_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken1'),
                InlineKeyboardButton(text='➡️', callback_data='chicken5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken3_inline':
            await call.message.answer(text="<b>Пита с куриным филе и корейской морковью (КБЖУ: 473/39/15/42)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/eYG7gHe8BDA?si=dMA56GHgzALicfId',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Пита с куриным филе и корейской морковью (КБЖУ: 473/39/15/42)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/eYG7gHe8BDA?si=dMA56GHgzALicfId',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )

    if call.data == 'chicken4' or call.data == 'chicken4_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken6'),
                InlineKeyboardButton(text='➡️', callback_data='chicken2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken4_inline':
            await call.message.answer(text="<b>Жульен с курицей и грибами (КБЖУ: 379/45/17/9)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/8LdMvtrj5FY?si=A4CnZckoN_YxgF-k',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Жульен с курицей и грибами (КБЖУ: 379/45/17/9)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/8LdMvtrj5FY?si=A4CnZckoN_YxgF-k',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )

    if call.data == 'chicken5' or call.data == 'chicken5_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken3'),
                InlineKeyboardButton(text='➡️', callback_data='chicken7')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken5_inline':
            await call.message.answer(text="<b>Боксмастер (КБЖУ: 457/32/18/18)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/Pk8WvsO7zow?si=YEAE2xcFfLHNO2NU',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Боксмастер (КБЖУ: 457/32/18/18)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/Pk8WvsO7zow?si=YEAE2xcFfLHNO2NU',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )
    if call.data == 'chicken6' or call.data == 'chicken6_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken6')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken7'),
                InlineKeyboardButton(text='➡️', callback_data='chicken4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken6_inline':
            await call.message.answer(text="<b>Куриное суфле с кабачком (КБЖУ: 232/25/11/9)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/fh9sVVfcrCI?si=TtQEbcG6ZUUgPhJr',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Куриное суфле с кабачком (КБЖУ: 232/25/11/9)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/fh9sVVfcrCI?si=TtQEbcG6ZUUgPhJr',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )

    if call.data == 'chicken7' or call.data == 'chicken7_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_chicken7')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='chicken5'),
                InlineKeyboardButton(text='➡️', callback_data='chicken6')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'chicken7_inline':
            await call.message.answer(text="<b>Шашлык из куриного филе (КБЖУ: 236/34/4/16)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/d8XWztLTBd4?si=wMlxeIr8U-wrnS8H',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )
        else:
            await call.message.edit_text(text="<b>Шашлык из куриного филе (КБЖУ: 236/34/4/16)</b>",
                                     parse_mode='html',
                                     link_preview_options=LinkPreviewOptions(
                                     url='https://youtube.com/shorts/d8XWztLTBd4?si=wMlxeIr8U-wrnS8H',
                                     prefer_large_media=True),
                                     reply_markup=keyboard
                                     )


@router.callback_query(F.data == 'recipe_chicken7')
@router.callback_query(F.data == 'recipe_chicken6')
@router.callback_query(F.data == 'recipe_chicken5')
@router.callback_query(F.data == 'recipe_chicken4')
@router.callback_query(F.data == 'recipe_chicken3')
@router.callback_query(F.data == 'recipe_chicken2')
@router.callback_query(F.data == 'recipe_chicken1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_chicken1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken1_inline')]
        ])
        await call.message.answer(text="""
                ИНГРЕДИЕНТЫ\n
- Куриное филе 450 г
- 2 яйца
- Соль, приправы, специи по вкусу
- 2 гречневых хлебца""")
        await call.message.answer(text="""
                ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ
                
1. <b>Подготовка курицы</b>: Порежьте куриное филе на тонкие кусочки. Если филе уже нарезано, пропустите этот шаг.
2. <b>Приготовление яичной смеси</b>: В миску разбейте яйцо. Добавьте соль, приправы и специи по вкусу. Хорошо перемешайте до однородного состояния.
3. <b>Приготовление панировки</b>: В блендере измельчите два хлебца до состояния крошек.
4. <b>Панировка курицы</b>: Каждый кусочек курицы сначала обмакните в яичную смесь, затем обваляйте в крошках из хлебцев.
5. <b>Запекание</b>: Выложите кусочки на противень. Далее их можно запечь в духовке до готовности (обычно около 20-30 минут при 180°C).

Подавать с любимым гарниром ❤️""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken2':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken2_inline')]
        ])
        await call.message.answer(text="""
                    ИНГРЕДИЕНТЫ\n
- салат айсберг,  
- соус (либо ZERO чесночный, либо медово-горчичный из Вкусвилла) 30 гр,  
- филе куриное 150 гр,  
- листы магги для нежного филе 1 шт,  
-томаты черри 60 гр
- сыр легкий 20 гр""")

        await call.message.answer(text="""
                    ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ
                    
1. Приготовить куриное филе можно несколькими способами:
- обжарить в листах магги или в пергаментной бумаге на сухой сковороде
- натереть смесью из специй и соли, завернуть в фольгу и запекать в разогретой до 180°С духовке 35-45 минут
- обжарить на антипригарной сковороде на капельке масла с добавлением соевого соуса
2. Выложить в миску все ингредиенты и перемешать."️""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken3_inline')]
        ])
        await call.message.answer(text="""
                        ИНГРЕДИЕНТЫ\n
- пита 55 гр 
- куриное филе (или филе индейки) 150 гр
- листы магги 1 шт (по желанию)
- томатный соус 50 г
- морковь по-корейски 70 г
- сыр плавленный 21 г""")

        await call.message.answer(text="""
                        ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ

    1. Приготовить куриное филе можно несколькими способами:
    - обжарить в листах магги или в пергаментной бумаге на сухой сковороде
    - натереть смесью из специй и соли, завернуть в фольгу и запекать в разогретой до 180°С духовке 35-45 минут
    - обжарить на антипригарной сковороде на капельке масла с добавлением соевого соуса
    2. Выложить в миску все ингредиенты и перемешать."️""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken4':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken4_inline')]
        ])
        await call.message.answer(text="""
    "Ингредиенты на две порции:\n 
Шампиньоны - 200 гр
Куриное филе - 350 гр
Соевый соус - 2 ст. л.
Масло сливочное - 5 гр
Лук - 100 гр
Сливки 20% - 70 гр
Сыр легкий - 30 гр""")

        await call.message.answer(text="""
                        ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ

1. Лук и шампиньоны нарезать, обжарить на масле 5-10 минут, добавить порезанную на мелкие кусочки курицу. Добавить соевый соус и если необходимо, то дополнительно посолить, поперчить. Когда курица станет белой со всех сторон, добавляем сливки, перемешиваем и снимаем с огня. 
2. Выкладываем все в формочки, либо в одну форму, посыпаем сыром и запекаем 15-20 минут в разогретой до 180 градусов духовке.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken5_inline')]
        ])
        await call.message.answer(text="""
        "Ингредиенты:\n

- тортилья 65 г (можно взять две маленькие по 30 гр)
- Творожный сыр 15 г
- Плавленный сыр Хохланд 25 г
- Филе куриное 100 г
- Листы для жарки Магги 7 г
- Соус: огурец соленый, горчица чайная ложка, чеснок 
- Овощи: салат айсберг, огурец, помидор""")

        await call.message.answer(text="""
                            РЕЦЕПТ ПРИГОТОВЛЕНИЯ

Куриную грудку завернуть в лист магги и обжарить на сковороде без масла, либо запечь в духовке.
Огурец нарезать соломкой, помидор дольками. Смазать тортилью творожным сыром, положить плавленный сыр, куриное филе, овощи, добавить соус, свернуть с нижнего края, затем с левого и затем с правого, запечь в гриле или на сковородке.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken6':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken6_inline')]
        ])
        await call.message.answer(text="""
            Ингредиенты на 4 порции:\n
- Кабачок 500 г
- Куриное филе 450 г
- Яйцо 2 Шт 
- Лук 100 г""")

        await call.message.answer(text="""
                                РЕЦЕПТ ПРИГОТОВЛЕНИЯ

1. Порезать кабачок, пропустить через блендер, можно отжать, переложить в миску.
2. Пропускаем лук и зубчик чеснока через блендер, добавить к кабачкам.
3. Порезать грудку, пропустить через блендер, добавить к кабачкам.
4. Перемешиваем все, добавляем яйцо, паприку, перец и соль
5. Выкладываем в форму, запекаем 35 минут при 180 градусах.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    elif call.data == 'recipe_chicken7':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='chicken7_inline')]
        ])
        await call.message.answer(text="""
                ИНГРЕДИЕНТЫ:

- Куриное филе 150 гр
- Соевый соус 100 мл
- Лук 50 гр
- Копченая паприка, приправа для курицы""")

        await call.message.answer(text="""
                                    РЕЦЕПТ ПРИГОТОВЛЕНИЯ

Куриное филе режем на кусочки, лук режем кольцами, выкладываем в миску, заливаем соевым соусом добавляем приправы, маринуем минимум 10 минут 

Курицу нанизываем на палочки, кладем в духовку на решетку над емкостью с водой, запекаем 10-15 минут, главное не передержать, иначе станет сухая.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)
