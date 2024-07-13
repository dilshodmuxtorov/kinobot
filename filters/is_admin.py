from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data import config
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        admins =  config.get_admin()
        return str(message.from_user.id) in admins