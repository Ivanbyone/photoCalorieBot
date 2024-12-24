""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()

@router.callback_query(F.data == 'ground_meat5')
@router.callback_query(F.data == 'ground_meat4')
@router.callback_query(F.data == 'ground_meat3')
@router.callback_query(F.data == 'ground_meat2')
@router.callback_query(F.data == 'ground_meat1')
@router.callback_query(F.data == 'ground_meat5_inline')
@router.callback_query(F.data == 'ground_meat4_inline')
@router.callback_query(F.data == 'ground_meat3_inline')
@router.callback_query(F.data == 'ground_meat2_inline')
@router.callback_query(F.data == 'ground_meat1_inline')
async def deserts(call: CallbackQuery):
    """ """
    if call.data == 'ground_meat1' or call.data == 'ground_meat1_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='ground_meat2'),
                InlineKeyboardButton(text='➡️', callback_data='ground_meat3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'ground_meat1_inline':
            await call.message.answer(text="<b>Запеканка с помидорами и сыром (2 порции) (КБЖУ на порцию: 399/50/18/9,2)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/kQSSgsBmQaE?si=FBiMRT-qEWAucTSa',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>Запеканка с помидорами и сыром (2 порции) (КБЖУ на порцию: 399/50/18/9,2)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/kQSSgsBmQaE?si=FBiMRT-qEWAucTSa',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )

    if call.data == 'ground_meat2' or call.data == 'ground_meat2_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='ground_meat4'),
                InlineKeyboardButton(text='➡️', callback_data='ground_meat1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'ground_meat2_inline':
            await call.message.answer(text="<b>Лазанья (КБЖУ: 328/34/8/27)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/ZmpC6SlPks0?si=7tdcC6-XhJwQK3d-',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>Лазанья (КБЖУ: 328/34/8/27)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/ZmpC6SlPks0?si=7tdcC6-XhJwQK3d-',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )

    if call.data == 'ground_meat3' or call.data == 'ground_meat3_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='ground_meat1'),
                InlineKeyboardButton(text='➡️', callback_data='ground_meat5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'ground_meat3_inline':
            await call.message.answer(text="<b>Тефтельки (КБЖУ: 43/11/20)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/ozak82ykEoc?si=1TVofg07Uq0PPREd',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>Тефтельки (КБЖУ: 43/11/20)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/ozak82ykEoc?si=1TVofg07Uq0PPREd',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )

    if call.data == 'ground_meat4' or call.data == 'ground_meat4_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='ground_meat5'),
                InlineKeyboardButton(text='➡️', callback_data='ground_meat2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'ground_meat4_inline':
            await call.message.answer(text="<b>Тортилья Чизбургер (КБЖУ: 310/20/13/26)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/AEpt7ktQdog?si=flmZvCh43Iqt-ZRZ',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>Тортилья Чизбургер (КБЖУ: 310/20/13/26)</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/AEpt7ktQdog?si=flmZvCh43Iqt-ZRZ',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )

    if call.data == 'ground_meat5' or call.data == 'ground_meat5_inline':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_ground_meat5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='ground_meat3'),
                InlineKeyboardButton(text='➡️', callback_data='ground_meat4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'ground_meat5_inline':
            await call.message.answer(text="<b>Пирог с мясным фаршем</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/botSQ1fS3cs?si=8IO6NdSm_Z-BtCO_',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )
        else:
            await call.message.edit_text(text="<b>Пирог с мясным фаршем</b>",
                                         parse_mode='html',
                                         link_preview_options=LinkPreviewOptions(
                                             url='https://youtube.com/shorts/botSQ1fS3cs?si=8IO6NdSm_Z-BtCO_',
                                             prefer_large_media=True),
                                         reply_markup=keyboard
                                         )


@router.callback_query(F.data == 'recipe_ground_meat5')
@router.callback_query(F.data == 'recipe_ground_meat4')
@router.callback_query(F.data == 'recipe_ground_meat3')
@router.callback_query(F.data == 'recipe_ground_meat2')
@router.callback_query(F.data == 'recipe_ground_meat1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_ground_meat1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='ground_meat1_inline')]
        ])
        await call.message.answer(text="""
                ИНГРЕДИЕНТЫ\n
- помидор
- Фарш из филе грудки (5%) 400 г
- Соус томатный 60 г
- сыр плавленный 2 шт
- сыр легкий 30 г
- йогурт греческий 80 г
- соль, копченая паприка, приправы по вкусу""")
        await call.message.answer(text="""
                ПОШАГОВЫЙ РЕЦЕПТ ПРИГОТОВЛЕНИЯ

- Выложите фарш в форму для запекания, посолите, поперчите и разровняйте
- Смажьте его томатной пастой
- Сверху выложите нарезанные кружочки помидоров, равномерно распределив их по фаршу.
- Смажьте греческим йогуртом, выложите плавленный сыр
- Посыпьте всё натертым сыром.

<b>Запекание</b>:

- Разогрейте духовку до 180°C.
- Поставьте форму с запеканкой в духовку и запекайте 25-30 минут, пока сыр не расплавится и не подрумянится.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)

    if call.data == 'recipe_ground_meat2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='ground_meat2_inline')]
            ])
            await call.message.answer(text="""
                    Ингредиенты на 4 порции:

- Листы для лазаньи - 128 гр 
- Лук 50 гр (по желанию)
- Фарш из мяса индейки (зеленая линия) - 500 гр
- Сыр 20% - 40 гр 
- Томатный соус Славянский дар - 150 гр
- сыр плавленный 2 ломтика 
""")
            await call.message.answer(text="""
                    Рецепт:
                    
1. Ставим разогреваться духовку на 220 градусов 
2. Фарш обжариваем с луком до золотистого цвета, вливаем в него томатный соус, тушим минут 10 
3. Трем сыр на крупной терке
4. Смазываем глубокий противень небольшим количеством соуса и выкладываем слои: листы для лазаньи, фарш, сыр и тд. Завершающий слой фарш и сыр
ВАЖНО!
Не кладите листы сухими, подержите их в кипятке по 2-3 минуты по одному (иначе они слипнутся)
5. Отправляем в духовку на 20 минут при 220 градусах""",
                                      parse_mode='html',
                                      reply_markup=keyboard)

    if call.data == 'recipe_ground_meat3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='ground_meat3_inline')]
        ])
        await call.message.answer(text="""
                    Ингредиенты:

- фарш Нежный из индейки - 500 гр;
- рис - 50 гр в сухом виде;
- яйцо - 1 шт;
- морковь - 100 гр;
- лук - 100 гр;
- томатная паста - 60 гр;
- соль, молотый перец, зелень по вкусу;
- сыр легкий - 40 гр;
- сметана 15% - 60 гр;
- чеснок - 2 зуб. ⠀""")
        await call.message.answer(text="""
                    Рецепт:

- рис отварить в подсоленной воде 10 мин, воду слить; 
- пока рис варится, на мелкой тёрке натереть морковь и лук (можно порезать); 
- филе перемолоть в фарш, добавить к нему рис, лук, морковь, яйцо. Посолить и поперчить по вкусу. Посыпать зеленью. Перемешать. 
- сформировать тефтели, выложить в противень; 
- томатную пасту развести стаканом воды, добавить сметану, пропущенный через пресс чеснок. Немного посолить. Перемешать. 
- залить тефтели соусом и отправить в духовку на 25 мин; 
- вытащить, посыпать тертым сыром и запекать ещё мин 10, чтобы сыр подрумянился. """,
                                  parse_mode='html',
                                  reply_markup=keyboard)

    if call.data == 'recipe_ground_meat4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='ground_meat4_inline')]
            ])
            await call.message.answer(text="""
                        Ингредиенты:

- лаваш/тортилья 40 гр 
- Фарш нежирный (можно перемолоть куриное филе) 60 гр
- сыр плавленный чизбургер
- соус: томатная паста (40 гр), греческий йогурт (40 гр) , горчица ( 5 г) и соленый огурчик⠀""")
            await call.message.answer(text="""
                        Рецепт:

Обязательно хорошо посолить и поперчить фарш, намазать его на тортилью и положить фаршем вниз на разогретую сковородку, жарить 5 минут, затем перевернуть и положить сыр и соус. """,
                                      parse_mode='html',
                                      reply_markup=keyboard)

    if call.data == 'recipe_ground_meat5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='ground_meat5_inline')]
        ])
        await call.message.answer(text="""
                            Ингредиенты:

- Фарш 300 гр ( 5% жирность, будьте внимательны при выборе фарша, обращайте внимание на количество жиров)
- Цветная капуста 400 гр
- Сливочное масло 5 гр
- Молоко 0,5% 80 гр
- Лук 100 гр
- Помидор 100 гр
- Сыр легкий арла натура 16% 36 гр
- Соус томатный для болоньезе 100 гр
- Приправа: сладкая паприка, перец⠀""")
        await call.message.answer(text="""
                            Рецепт:
                            
- Режем лук, тушим на сковороде 5 минут, добавляем фарш, солим, перчим, тушим еще 5 минут и добавляем соус, оставляем минут на 10 тушиться.

- Отвариваем цветную капусту в подсоленной воде, перекладываем в чашу блендера, взбиваем с молоком и маслом. После пробуем и если нужно еще подсаливаем.

- В форму выкладываем фарш, пюре из цветной капусты, помидоры, натертый сыр и в духовку на 25-30 минут при 180 градусах.""",
                                  parse_mode='html',
                                  reply_markup=keyboard)
