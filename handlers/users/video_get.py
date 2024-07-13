from aiogram import types
from loader import dp
from utils.db_api.db_commands import get_video
from utils.style import html
from data import config

@dp.message_handler(lambda message: str(message.text).isdigit() and len(str(message.text).split()) == 1)
async def get_message_id_handler(message: types.Message):
    code = int(message.text)
    if get_video(code):
        await message.answer_video(video=get_video(code),caption=f"👇👇Ushbu kanalga a'zo bo'ling\n\n{config.CHANNEL}")
    else:
        await message.answer(html.italic("❌Bu kodda video mavjud emas. To'g'ri kod kiriting "))
    
    