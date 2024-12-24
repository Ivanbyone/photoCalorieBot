from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()


@router.callback_query(F.data == 'salads5')
@router.callback_query(F.data == 'salads4')
@router.callback_query(F.data == 'salads3')
@router.callback_query(F.data == 'salads2')
@router.callback_query(F.data == 'salads1')
@router.callback_query(F.data == 'salads_inline5')
@router.callback_query(F.data == 'salads_inline4')
@router.callback_query(F.data == 'salads_inline3')
@router.callback_query(F.data == 'salads_inline2')
@router.callback_query(F.data == 'salads_inline1')
async def salads(call: CallbackQuery):
    """ """
    if call.data == 'salads1' or call.data == 'salads_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='salads2'),
                InlineKeyboardButton(text='➡️', callback_data='salads3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'salads_inline1':
            await call.message.answer(text="<b>Салат с креветками, рукколой и киноа (КБЖУ: 316/20/10/35) </b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/TXynF6Ra008?si=6EgnV8l_oKmi3yN4',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Салат с креветками, рукколой и киноа (КБЖУ: 316/20/10/35) </b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/TXynF6Ra008?si=6EgnV8l_oKmi3yN4',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'salads2' or call.data == 'salads_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='salads4'),
                InlineKeyboardButton(text='➡️', callback_data='salads1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'salads_inline2':
            await call.message.answer(text="<b>ПОКЕ с рисом, тунцом и креветками (КБЖУ: 449/20/14/56)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                      url='https://youtube.com/shorts/bF4_J4Y4oBY?si=mrQmEhjVxVF9hpak',
                                      prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>ПОКЕ с рисом, тунцом и креветками (КБЖУ: 449/20/14/56)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/bF4_J4Y4oBY?si=mrQmEhjVxVF9hpak',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'salads3' or call.data == 'salads_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='salads1'),
                InlineKeyboardButton(text='➡️', callback_data='salads5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'salads_inline3':
            await call.message.answer(text="<b>Салат со свеклой и брынзой (КБЖУ: 292/12/15/25)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/k_XWtiHzwJs?si=TFUWTYM8FUAGCpEM',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Салат со свеклой и брынзой (КБЖУ: 292/12/15/25)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/k_XWtiHzwJs?si=TFUWTYM8FUAGCpEM',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'salads4' or call.data == 'salads_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='salads5'),
                InlineKeyboardButton(text='➡️', callback_data='salads2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'salads_inline4':
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

    if call.data == 'salads5' or call.data == 'salads_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_salads5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='salads3'),
                InlineKeyboardButton(text='➡️', callback_data='salads4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'salads_inline5':
            await call.message.answer(text="<b>Салат из красной фасоли с грудкой и сухариками (КБЖУ: 487/30/15/55)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/HUK1elDtoIA?si=BrdlO2kgoaR0FpMA',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Салат из красной фасоли с грудкой и сухариками (КБЖУ: 487/30/15/55)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/HUK1elDtoIA?si=BrdlO2kgoaR0FpMA',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_salads5')
@router.callback_query(F.data == 'recipe_salads4')
@router.callback_query(F.data == 'recipe_salads3')
@router.callback_query(F.data == 'recipe_salads2')
@router.callback_query(F.data == 'recipe_salads1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_salads1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='salads_inline1')]
        ])
        await call.message.answer(text=""" 
               Ингредиенты: 
- Айсберг и руккола (я их не взвешиваю)
- Киноа 40 гр в сухом виде (половина пакетика)
- Креветки 80 гр (очищенные)
- Апельсин 100 гр (можно манго)
- Соус ореховый Tamaki 15 гр
Если нет соуса, то 1 ч.л. оливкового масла, 1 ч.л. соевого соуса, сок лимона и апельсина.
""",
                                  protect_content=True)
        await call.message.answer(text="""
                Приготовление:
1. Киноа отварить (если в пакетике, то опустить в кипящую воду на 20 минут)
2. Креветки отварить (можно вместе с киноа)
3. Апельсин порезать на маленькие кусочки
4. Выложить на тарелку салатную смесь, соус, перемешать, сверху добавить киноа, апельсин и креветки, перемешать и наслаждаться.


""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_salads2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='salads_inline2')]
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

Приготовление:
1. Креветки отварить в кипящей подсоленной воде 3 минуты;
2. Рис отварить до готовности (я беру в пакетиках и варю в кипящей подсоленной воде 25 минут);
3. Манго, авокадо порезать кубиками, огурец –соломкой;
4. Соединить все ингредиенты в глубокой тарелке секторами, полить соусами;
5. Сверху порезать стружкой нори или посыпать кунжутом

 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_salads3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='salads_inline3')]
        ])
        await call.message.answer(text="""
		Ингредиенты: 
- Руккола 
- свекла 200 г
- Орехи кедровые 10 г
- Брынза сербская (у моей КБЖУ 200/13/14/4) 60 г
- Соус бальзамический Tamaki 20 г
     """,
                                  protect_content=True)
        await call.message.answer(text="""
Приготовление: 
1. Свеклу отварить (по времени ≈ час, можно купить готовую) и порезать,
2. фетаксу/брынзу порезать на кубики,
3. смешать все с рукколой и кедровыми орешками,
4. полить бальзамическим соусом,
5. Наслаждаться ❤                        """,
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_salads4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='salads_inline4')]
            ])
            await call.message.answer(text="""
         Ингредиенты:
- салат айсберг, 
- соус (либо ZERO чесночный, либо медово-горчичный из Вкусвилла) 30 гр, 
- филе куриное 150 гр, 
- листы магги для нежного филе 1 шт, 
-томаты черри 60 гр
- сыр легкий 20 гр
""",
                                      protect_content=True)
            await call.message.answer(text="""
		Приготовление:
1. Приготовить куриное филе можно несколькими способами:
- обжарить в листах магги или в пергаментной бумаге на сухой сковороде
- натереть смесью из специй и соли, завернуть в фольгу и запекать в разогретой до 180°С духовке 35-45 минут
- обжарить на антипригарной сковороде на капельке масла с добавлением соевого соуса
2. Выложить в миску все ингредиенты и перемешать.

 """,
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_salads5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='salads_inline5')]
        ])
        await call.message.answer(text="""
  	Ингредиенты:
- Красная фасоль в соусе (у меня бондюель в соусе Чили) - 170 гр
- Кукуруза консервированная - 70 гр
- Филе индейки копченое/ветчина/куриная грудка (у меня куриное филе в листах магги) - 70 гр
- Гренки/сухарики - 20 гр
- маринованный огурчик (по желаию)
- Можно еще добавить: кинзу, сметану, корейскую морковь, помидоры черри по желанию

    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
Все смешать и наслаждаться ❤

""",
                                  reply_markup=keyboard,
                                  protect_content=True)
