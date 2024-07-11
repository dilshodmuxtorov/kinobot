from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        admins = [5645617968]  
        return message.from_user.id in admins