from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp , bot
from filters.is_admin import IsAdmin
from utils.db_api.db_commands import count_video, count_user , get_all_user ,set_inactive , active_users , inactive_users, get_video ,delete_video
from utils.style import html
from states.add_video_state import MessageState ,DeleteVideoState
from keyboards.inline.confirm import confirm_btn
from aiogram.utils.exceptions import BotBlocked, BadRequest





@dp.message_handler(lambda message: message.text == "📊 Statistika")
async def button_handler(message: types.Message):
    if await IsAdmin().check(message):
        users = count_user()
        videos = count_video()
        active_user = active_users()
        inactive_user = inactive_users()
        text = f"""
🗒{html.bold("All users ")}: {html.bold(users)},

♻️{html.italic("Active users")}: {html.bold(active_user)}
⭕️{html.italic("Inactive users")}: {html.bold(inactive_user)}

📹{html.bold("Videos")} : {html.bold(videos)}
    """
        await message.answer(text=text)

@dp.message_handler(lambda message: message.text == "📤Send message to users")
async def button_handler(message: types.Message):
    if await IsAdmin().check(message):
        await MessageState.message.set()
        await message.answer("Please enter the message you want to send to all users.")

@dp.message_handler(state=MessageState.message)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_to_send'] = message.text  
    await MessageState.confirm.set()
    await message.answer(f"You want to send the following message to all users:\n\n{message.text}", reply_markup=confirm_btn)
 
@dp.callback_query_handler(lambda c: c.data in ['confirm_yes', 'confirm_no'], state=MessageState.confirm)
async def process_callback_confirm(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        message_to_send = data['message_to_send']

    if callback_query.data == 'confirm_yes':
        users = get_all_user()  
        count = 1
        for user_id in users:           
            if count%1001 == 0:
                await bot.send_message(callback_query.from_user.id, html.italic(f" Message have been sent to {count} users."))            
            try:
                await bot.send_message(chat_id=user_id[0], text=message_to_send)
                count = count+1
            except BotBlocked:
                set_inactive(user_id=int(user_id[0]))

        await bot.send_message(callback_query.from_user.id, html.bold(f"✅ Message sent to all {count-1} users."))
    else:
        await bot.send_message(callback_query.from_user.id, html.bold("❌Message not sent."))
    
    await bot.answer_callback_query(callback_query.id)
    await state.finish()

# @dp.message_handler(lambda message: message.text == "🚮Delete video")
# async def button_handler(message: types.Message):
#     if await IsAdmin().check(message):
#         await DeleteVideoState.code.set()
#         await message.answer("Send a code you want to delete a video")

# @dp.message_handler(state=DeleteVideoState.code)
# async def process_message(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['message_to_send'] = message.text  
#         try:
#             video_id = get_video(int(message.text))
#         except BadRequest:
#             await message.answer(html.bold("There is no video in this code!"))
#     await DeleteVideoState.confirm.set()
#     await message.answer_video(video=video_id,caption=f"Are you sure to delete this video {message.text}?",reply_markup=confirm_btn)
 
# @dp.callback_query_handler(lambda c: c.data in ['confirm_yes', 'confirm_no'], state=DeleteVideoState.confirm)
# async def process_callback_confirm(callback_query: types.CallbackQuery, state: FSMContext):
#     async with state.proxy() as data:
#         video_id= data['message_to_send']
    
#     if callback_query.data == 'confirm_yes':
#         if video_id:
#             delete_video(int(video_id))
#             await bot.send_message(callback_query.from_user.id, html.bold("✔️ Video deleted."))
#         else:
#             await bot.send_message(callback_query.from_user.id, html.bold("❌ Unable to delete video."))
#     else:
#         await bot.send_message(callback_query.from_user.id, html.bold("❌ Video not deleted."))
  
#     await bot.answer_callback_query(callback_query.id)
#     await state.finish()

@dp.message_handler(lambda message: message.text == "🚮Delete video")
async def button_handler(message: types.Message):
    if await IsAdmin().check(message):
        await DeleteVideoState.code.set()
        await message.answer("Send a code you want to delete a video")

@dp.message_handler(state=DeleteVideoState.code)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message_to_send'] = message.text  
        try:
            video_id = int(message.text)  
            video_info = get_video(int(video_id))
            if video_info:
                await DeleteVideoState.confirm.set()
                await message.answer_video(
                    video=video_info, 
                    caption=f"Are you sure to delete this video\n\nCode: {message.text}",  
                    reply_markup=confirm_btn
                )
            else:
                await message.answer(html.bold("There is no video with this code!"))
                await state.finish()
        except ValueError:
            await message.answer(html.bold("Invalid code format! Please send a valid code."))

@dp.callback_query_handler(lambda c: c.data in ['confirm_yes', 'confirm_no'], state=DeleteVideoState.confirm)
async def process_callback_confirm(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        video_id = data['message_to_send']
    
    if callback_query.data == 'confirm_yes':
        try:
            # Assuming delete_video function handles video deletion
            delete_video(int(video_id))
            await bot.send_message(callback_query.from_user.id, html.bold("✔️ Video deleted."))
        except Exception as e:
            print(f"Error deleting video: {e}")
            await bot.send_message(callback_query.from_user.id, html.bold("❌ Unable to delete video."))
    else:
        await bot.send_message(callback_query.from_user.id, html.bold("❌ Video not deleted."))

    await bot.answer_callback_query(callback_query.id)
    await state.finish()