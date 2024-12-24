
from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, LinkPreviewOptions

router = Router()

@router.callback_query(F.data == 'cheese5')
@router.callback_query(F.data == 'cheese4')
@router.callback_query(F.data == 'cheese3')
@router.callback_query(F.data == 'cheese2')
@router.callback_query(F.data == 'cheese1')
@router.callback_query(F.data == 'cheese_inline5')
@router.callback_query(F.data == 'cheese_inline4')
@router.callback_query(F.data == 'cheese_inline3')
@router.callback_query(F.data == 'cheese_inline2')
@router.callback_query(F.data == 'cheese_inline1')
async def deserts(call: CallbackQuery):
    """ """
    if call.data == 'cheese1' or call.data == 'cheese_inline1':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese1')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='cheese2'),
                InlineKeyboardButton(text='➡️', callback_data='cheese3')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'cheese_inline1':
            await call.message.answer(text="<b> Творожные бейглы с ветчиной и сыром (КБЖУ: 398/38/15/28)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/qMQ6y1GWddE?si=1UAca8JalCdyT12s',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b> Творожные бейглы с ветчиной и сыром (КБЖУ: 398/38/15/28)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/qMQ6y1GWddE?si=1UAca8JalCdyT12s',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'cheese2' or call.data == 'cheese_inline2':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese2')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='cheese4'),
                InlineKeyboardButton(text='➡️', callback_data='cheese1')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'cheese_inline2':
            await call.message.answer(text="<b>Сырники с рикоттой (КБЖУ: 450/33/15/44)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/Np1TL7Ec3rI?si=KXG3-HcwuLSoijEa',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Сырники с рикоттой (КБЖУ: 450/33/15/44)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/Np1TL7Ec3rI?si=KXG3-HcwuLSoijEa',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'cheese3' or call.data == 'cheese_inline3':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese3')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='cheese1'),
                InlineKeyboardButton(text='➡️', callback_data='cheese5')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'cheese_inline3':
            await call.message.answer(text="<b>Сырная лепешка (КБЖУ: 547/51/21/34)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://www.youtube.com/shorts/pnwDD1ctLVg',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Сырная лепешка (КБЖУ: 547/51/21/34)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://www.youtube.com/shorts/pnwDD1ctLVg',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'cheese4' or call.data == 'cheese_inline4':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese4')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='cheese5'),
                InlineKeyboardButton(text='➡️', callback_data='cheese2')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'cheese_inline4':
            await call.message.answer(text="<b>Творожные ватрушки с творогом (КБЖУ: 250/28/5/24)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/qJl78HexW4o?si=fr2HsuJQ6qxykAwb',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Творожные ватрушки с творогом (КБЖУ: 250/28/5/24)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/qJl78HexW4o?si=fr2HsuJQ6qxykAwb',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )

    if call.data == 'cheese5' or call.data == 'cheese_inline5':

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Рецепт', callback_data='recipe_cheese5')],
            [
                InlineKeyboardButton(text='⬅️', callback_data='cheese3'),
                InlineKeyboardButton(text='➡️', callback_data='cheese4')
            ],
            [InlineKeyboardButton(text='Назад', callback_data='button_recipe_analyse_pressed')]
        ])
        if call.data == 'cheese_inline5':
            await call.message.answer(text="<b>Запеканка из рикотты с грушей (КБЖУ на порцию: 262/16/11/22)</b>",
                                      parse_mode='html',
                                    link_preview_options=LinkPreviewOptions(
                                    url='https://youtube.com/shorts/9RLKvZi4ZvQ?si=Q882tUKIAkFxbhM1',
                                    prefer_large_media=True),
                                    reply_markup=keyboard
                                    )
        else:
            await call.message.edit_text(text="<b>Запеканка из рикотты с грушей (КБЖУ на порцию: 262/16/11/22)</b>",
                                      parse_mode='html',
                                      link_preview_options=LinkPreviewOptions(
                                          url='https://youtube.com/shorts/9RLKvZi4ZvQ?si=Q882tUKIAkFxbhM1',
                                          prefer_large_media=True),
                                      reply_markup=keyboard
                                      )


@router.callback_query(F.data == 'recipe_cheese5')
@router.callback_query(F.data == 'recipe_cheese4')
@router.callback_query(F.data == 'recipe_cheese3')
@router.callback_query(F.data == 'recipe_cheese2')
@router.callback_query(F.data == 'recipe_cheese1')
async def recipe_chicken(call: CallbackQuery) -> None:
    """ """
    if call.data == 'recipe_cheese1':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='cheese_inline1')]
        ])
        await call.message.answer(text=""" 
Ингредиенты для двух бейлов: 
- творог 2% 180 гр 
- яйцо куриное 54 
- сыр легкий 20 гр 
- рисовая мука 60 гр 
- соль, перец, сушеные травы, зелень (укроп) по желанию 
Начинка на один бейгл: 
- Ветчина индилайт 30 г 
- Яйцо куриное 54 г 
- Сыр творожный 10 г """,
                                  protect_content=True)
        await call.message.answer(text="""
                Рецепт:
К творогу добавляем яйцо, муку, сушеные травы, соль по вкусу. Замешиваем тесто и делим на две равные части. Раскатываем колбаску и сворачиваем в бейгл. Смазываем желтком, отправляем в разогретую духовку. Выпекаем 180 градусов 20 минут. Достаем, разрезаем на две части. Смазываем творожным сыром, выкладываем ветчину, рукколу, яйцо.
""",
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_cheese2':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='cheese_inline2')]
            ])
            await call.message.answer(text="""
                    Ингредиенты:
- творог в брикете 0-2% 100 г 
- рикотта лайт (у меня ВкусВилл) 100 г 
-желток 
- сироп топинамбура 15 г 
-мука рисовая 40 г 
- сахарозаменитель (фит парад)
""",
                                      protect_content=True)
            await call.message.answer(text="""
                    Рецепт:
Смешать все ингредиенты, скатать СЫРЫМИ руками в шарики и выложить на ГОРЯЧУЮ сковороду. Жарить по 3 минутки с каждой стороны ПОД КРЫШКОЙ.(Если сковорода антипригарная, то можно жарить без масла)
""",
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_cheese3':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='cheese_inline3')]
        ])
        await call.message.answer(text="""
                        Ингредиенты:

- 180 г творог 5% 
- 40-50 г рисовой муки 
- 1 яйцо 
- сыр (лёгкий 15%) ≈ 50 г 
- соль, перец, укроп

""",
                                  protect_content=True)
        await call.message.answer(text="""
Вариант №1: Выложить на разогретую сковородку. Обжарить по несколько минут с каждой стороны. 
Вариант №2: Сформировать лодочку, запечь в духовке. Можно сделать ямку и туда положить желток и еще посыпать сверху сыром.
                        """,
                                  reply_markup=keyboard,
                                  protect_content=True)

    if call.data == 'recipe_cheese4':
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='Назад', callback_data='cheese_inline4')]
            ])
            await call.message.answer(text="""
Ингредиенты на 2 порции: 
- творог в брикете Простоквашино 2% 180 г 
- яйцо С1 (в тесто только белок) 
- мука рисовая 40 г 
- 1/4 чайной ложки разрыхлителя 
- мягкий творог ( у меня Савушкин 0,1%) 125 г 
- сахарозаменитель (фит парад) 
- ягоды 30 г (у меня голубика свежая)
""",
                                      protect_content=True)
            await call.message.answer(text="""
                        Рецепт:
1. Белок хорошенько смешать с творогом. 
2. Добавить подсластитель (у меня 1 пакетик фитпарада), муку, разрыхлитель, все смешать. 
3. Мокрыми руками разделить на 4 шарика и выложить на пергамент или силиконовый коврик. ВАЖНО ❗️❗️❗️ Если используете пергамент, то смажьте его маслом, но учтите его в общей калорийности. 4.Приплюснуть их на пергаменте мокрым стаканом и мокрыми руками сделать углубления. 
5.Мягкий творог смешать с подсластителем (у меня 1 пакетик фитпарада), распределить по ватрушкам, а сверху положить ягоды. 
6.Отправить в разогретую до 180 градусов духовку на 20-25 минут до румяности.
""",
                                      reply_markup=keyboard,
                                      protect_content=True)

    if call.data == 'recipe_cheese5':
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='cheese_inline5')]
        ])
        await call.message.answer(text="""
                            Ингредиенты:
- рикотта 250г 
- творог 5% 180 г 
- яйцо 2 шт 
- кукурузный крахмал 60г 
- сахарозаменитель (у меня Fitparad) 
- груша конференция
    """,
                                  protect_content=True)
        await call.message.answer(text="""
                            Рецепт:
1.	Белки отделяем от желтка, и отдельно белки взбиваем в пену с сах/замом. 
2.	Смешиваем желток, творог, рикотту и просеиваем к ним крахмал. 
3.	Аккуратно вмешиваем белки, выкладываем в форму и сверху раскладываем произвольно грушу 🍐 
4.	Отправляем в духовку 140* на 50-60 минут (смотрим на корочку). 
5.	Даем остыть и убираем настояться в холодильник!
""",
                                  reply_markup=keyboard,
                                  protect_content=True)


