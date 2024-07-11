from loader import dp
from aiogram import types
from filters.is_admin import IsAdmin
from utils.style.styles import bold
from utils.db_api.db_commands import count_video, count_user

@dp.message_handler(lambda message: message.text == "📊 Statistika")
async def button_handler(message: types.Message):
    if await IsAdmin().check(message):
        users = count_user()
        videos = count_video()
        text = f"""
{bold("Foydalanuvchilar soni ")}: {users},
{bold("Videolar soni")} : {videos}
    """
        await message.answer(text=text)