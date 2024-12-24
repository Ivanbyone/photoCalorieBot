''' '''
import datetime

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, PreCheckoutQuery, Message
from aiogram.types.labeled_price import LabeledPrice

from data.dbconnect import mongoBase

router = Router()


@router.callback_query(F.data == 'recipe_payments')
async def pay_for_recipes(call:CallbackQuery) -> None:
    ''' '''
    date = await mongoBase.check_recipe_subscription(tg_id=call.message.chat.id)

    if date != None and date > datetime.datetime.utcnow():
        await call.answer(text='У вас уже есть эта подписка.',
                          show_alert=True)
    else:
        prices = [LabeledPrice(label="XTR", amount=499)]

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Оплатить 499 ⭐", pay=True)],
            [InlineKeyboardButton(text='Отменить', callback_data='cancel_payment')]
        ])

        await call.message.answer_invoice(title="Оплатить доступ к базе с рецептами",
                                          prices=prices,
                                          description=f"Оплатить доступ к базе с рецептами\n(499 Telegram stars)",
                                          provider_token="",
                                          payload=f"recipes_pay",
                                          currency='XTR',
                                          reply_markup=keyboard)


@router.callback_query(F.data == 'photo_payments25')
@router.callback_query(F.data == 'photo_payments10')
@router.callback_query(F.data == 'photo_payments1')
async def photo_payments(call:CallbackQuery) -> None:
    ''' '''

    subscription = await mongoBase.check_photo_attempts(tg_id=call.message.chat.id)

    if subscription != None and subscription != 0:
        await call.answer(text='У вас еще есть попытки.',
                          show_alert=True)
    else:
        if call.data == 'photo_payments1':
            prices = [LabeledPrice(label="XTR", amount=7)]

            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить 7 ⭐", pay=True)],
                [InlineKeyboardButton(text='Отменить', callback_data='cancel_payment')]
            ])

            await call.message.answer_invoice(title="Оплатить 1 поиск по фото",
                                              prices=prices,
                                              description=f"Оплатить 1 поиск по фото\n(7 Telegram stars)",
                                              provider_token="",
                                              payload=f"photo_pay1",
                                              currency='XTR',
                                              reply_markup=keyboard)
        elif call.data == 'photo_payments10':
            prices = [LabeledPrice(label="XTR", amount=70)]

            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить 70 ⭐", pay=True)],
                [InlineKeyboardButton(text='Отменить', callback_data='cancel_payment')]
            ])

            await call.message.answer_invoice(title="Оплатить 10 поисков по фото",
                                              prices=prices,
                                              description=f"Оплатить 10 поисков по фото\n(70 Telegram stars)",
                                              provider_token="",
                                              payload=f"photo_pay10",
                                              currency='XTR',
                                              reply_markup=keyboard)

        elif call.data == 'photo_payments25':
            prices = [LabeledPrice(label="XTR", amount=175)]

            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Оплатить 175 ⭐", pay=True)],
                [InlineKeyboardButton(text='Отменить', callback_data='cancel_payment')]
            ])

            await call.message.answer_invoice(title="Оплатить 25 поисков по фото",
                                              prices=prices,
                                              description=f"Оплатить 25 поисков по фото\n(175 Telegram stars)",
                                              provider_token="",
                                              payload=f"photo_pay25",
                                              currency='XTR',
                                              reply_markup=keyboard)


@router.pre_checkout_query()
async def on_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


@router.message(F.successful_payment)
async def successful_recipes_payment(message: Message, bot: Bot) -> None:
    ''' '''
    payload = message.successful_payment.invoice_payload

    if payload == "recipes_pay":

        await mongoBase.save_recipe_payment(tg_id=message.from_user.id, username=message.from_user.username,transaction=message.successful_payment.telegram_payment_charge_id)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pay_button_pressed')]
        ])

        await bot.send_message(chat_id=message.from_user.id,
                               text='Оплата прошла успешно.\nСпасибо за покупку!',
                               reply_markup=keyboard)

        await bot.delete_message(message.chat.id, message.message_id)


    elif payload == "photo_pay1":
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

    elif payload == "photo_pay10":

        await mongoBase.save_photo_payment(tg_id=message.from_user.id, username=message.from_user.username,
                                           transaction=message.successful_payment.telegram_payment_charge_id,
                                           attempts=10)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pay_button_pressed')]
        ])

        await bot.send_message(chat_id=message.from_user.id,
                               text='Оплата прошла успешно.\nСпасибо за покупку!',
                               reply_markup=keyboard)

        await bot.delete_message(message.chat.id, message.message_id)

    elif payload == "photo_pay25":

        await mongoBase.save_photo_payment(tg_id=message.from_user.id, username=message.from_user.username,
                                           transaction=message.successful_payment.telegram_payment_charge_id,
                                           attempts=25)

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Назад', callback_data='pay_button_pressed')]
        ])

        await bot.send_message(chat_id=message.from_user.id,
                               text='Оплата прошла успешно.\nСпасибо за покупку!',
                               reply_markup=keyboard)

        await bot.delete_message(message.chat.id, message.message_id)
