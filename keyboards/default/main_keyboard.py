from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_bt = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📤Send message to users"),KeyboardButton('📊 Statistika')],
        [KeyboardButton("🚮Delete video")],
    ]
    ,resize_keyboard=True
)
