""" Starting bot """
import asyncio
import logging

from config.config import bot, dp
from handlers.main_commands import commands
from handlers.callbacks import photo_analyse, user_profile, info, helper
from handlers.callbacks.recipes import recipe_callback, deserts, chicken, ground_meat, oatmeal, cheese, roll, avocado, tuna, salads, pancakes, eggs
from handlers.callbacks.payments import payments, recipe_payments, photo_payments
from utils.command_helper import set_commands

bot_logger = logging.getLogger(__name__)


async def main() -> None:
    """
    function for starting bot
    :return: None
    """

    # Config for logging events
    logging.basicConfig(
        level=logging.WARNING,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Level info for starting Bot
    bot_logger.info('Bot has been started...')

    dp.include_routers(
        commands.router,
        photo_analyse.photo_analyse,
        user_profile.profile,
        info.info_router,
        recipe_callback.recipes,
        payments.router,
        recipe_payments.router,
        deserts.router,
        chicken.router,
        ground_meat.router,
        oatmeal.router,
        cheese.router,
        roll.router,
        avocado.router,
        tuna.router,
        salads.router,
        pancakes.router,
        eggs.router,
        helper.helper_router
    )

    dp.startup.register(set_commands)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Starting bot failed with {e}")
