from aiogram.types import  InlineKeyboardMarkup, InlineKeyboardButton


confirm_btn= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅ Yes", callback_data='confirm_yes'),InlineKeyboardButton("❌ No", callback_data='confirm_no')
        ]
    ]    
)