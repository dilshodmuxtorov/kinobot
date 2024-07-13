import logging

from aiogram import Dispatcher

from data.config import get_admin, ADMINS


async def on_startup_notify(dp: Dispatcher):
    admins = get_admin()
    print(ADMINS)
    print(admins)
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")
            print(admin)

        except Exception as err:
            logging.exception(err)
