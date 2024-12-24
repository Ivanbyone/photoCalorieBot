''' '''

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, PreCheckoutQuery, Message, ContentType
from aiogram.types.labeled_price import LabeledPrice

from data.dbconnect import mongoBase
from utils.FSM_states import FsmStates

router = Router()


@router.callback_query(F.data == 'photo_payments1')
async def photo_payments(call:CallbackQuery, state: FSMContext) -> None:
    ''' '''
    if call.data == 'photo_payments1':
        prices = [LabeledPrice(label="XTR", amount=1)]

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Оплатить 7 ⭐", pay=True)],
            [InlineKeyboardButton(text='Отменить', callback_data='cancel_payment')]
        ])

        await call.message.answer_invoice(title="Payment 7 stars",
                                          prices=prices,
                                          description=f"Оплатить 1 поиск по фото\n(7 Telegram stars)",
                                          provider_token="",
                                          payload=f"photo_pay1",
                                          currency='XTR',
                                          reply_markup=keyboard)


@router.message(F.successfull_payment)
async def successful_recipes_payment(message: Message, bot: Bot) -> None:
    ''' '''
    payload = message.successful_payment.invoice_payload

    if payload == "photo_pay1":
        await bot.refund_star_payment(
            user_id=message.from_user.id,
            telegram_payment_charge_id=message.successful_payment.telegram_payment_charge_id
        )

        await mongoBase.save_photo_payment(tg_id=message.from_user.id, username=message.from_user.username,
                                           transaction=message.successful_payment.telegram_payment_charge_id,
                                           attempts=1)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pay_button_pressed')]
        ])

        await bot.send_message(chat_id=message.from_user.id,
                               text='Оплата прошла успешно.\nСпасибо за покупку!',
                               reply_markup=keyboard)

        await bot.delete_message(message.chat.id, message.message_id)
