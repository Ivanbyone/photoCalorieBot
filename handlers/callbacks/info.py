""" """

from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

info_router = Router()


@info_router.callback_query(F.data == "big_button_3_pressed")
async def send_important_info(call: CallbackQuery) -> None:
    """
    Message for callback from "Важная информация" button
    :param call: callback from main menu
    :return: None
    """

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='/start')]
    ])

    await call.message.edit_text(text='Важная информация доступна по ссылкам:\n\n<a href="https://telegra.ph/Poshagovaya-shema-kak-nachat-menyat-svoj-racion-dlya-pohudeniya-09-02">✅ Пошаговая схема как начать менять свой рацион для похудения</a>\n\n<a href="https://telegra.ph/Treker-dlya-otslezhivaniya-progressa-09-23">✅ Трекер для отслеживания прогресса</a>\n\n<a href="https://telegra.ph/Belok---zalog-kachestvennogo-pohudeniya-09-23">✅ Белок - залог качественного похудения</a>',
                                 parse_mode='html',
                                 disable_web_page_preview=True,
                                 reply_markup=keyboard)
