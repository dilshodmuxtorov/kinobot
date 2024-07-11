from loader import dp
from aiogram import types
from filters.is_admin import IsAdmin
from utils.style.styles import bold
from utils.db_api.db_commands import add_video



@dp.message_handler(content_types=types.ContentType.VIDEO)
async def video_handler(message: types.Message, ):
    if await IsAdmin().check(message=message):
        video_id = message.video.file_id
        try:
            code = add_video(video_id)
            await message.answer(bold(f"✅ Video added successfully with code: {code}"))
        except:
            await message.answer("Video databazaga qo'shilmadi!")
    else:
        await message.answer("❌ "+bold("Xato xabar!"))

