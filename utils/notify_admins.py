import logging

from aiogram import Dispatcher

from data.config import  ADMINS
from aiogram.utils.exceptions import BotBlocked

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Bot ishga tushdi")
        except (Exception, BotBlocked) as err:
            pass

