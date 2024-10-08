from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from filters import IsAdmin
from utils.db_api.db_commands import add_user_to_db ,count_video
from utils.style import html
from keyboards.default.main_keyboard import main_bt

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    if await IsAdmin().check(message):
        await message.answer(html.bold(f"Salom Admin {message.from_user.full_name}, botga xush kelibsiz!"),reply_markup=main_bt)
    else:
        add_user_to_db(message.from_user.id,message.from_user.username, message.from_user.full_name)
        count = count_video()
        text =html.bold(f"""Salom {message.from_user.full_name},botga xush kelibsiz!""")+html.italic(f"""

Kino kodini kiriting (1 dan {count} gacha), 
Bot sizga o'sha videoni tashab beradi.
""" )
        await message.answer(text)