''' '''

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


@router.callback_query(F.data == 'cancel_payment')
@router.callback_query(F.data == 'pay_button_pressed')
async def payments_menu(call: CallbackQuery, bot: Bot, state: FSMContext) -> None:
    ''' '''

    await state.clear()

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 поиск по фото (7 ⭐)', callback_data='photo_payments1')],
        [InlineKeyboardButton(text='10 поисков по фото (70 ⭐)', callback_data='photo_payments10')],
        [InlineKeyboardButton(text='25 поиск по фото (175 ⭐)', callback_data='photo_payments25')],
        [InlineKeyboardButton(text='Доступ к рецептам (499 ⭐)', callback_data='recipe_payments')],
        [InlineKeyboardButton(text='Назад', callback_data='/start')]
    ])

    if call.data == 'cancel_payment':
        await call.message.answer(text='Выбери предложение',
                                  reply_markup=keyboard)
        await bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        await call.message.edit_text(text='Выбери предложение',
                                     reply_markup=keyboard)
