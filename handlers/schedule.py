# from aiogram import types
# from config import bot, scheduler
#
#
# async def handle_schedule(message: types.Message):
#     scheduler.add_job(
#         send_notif(),
#         "interval",
#         seconds=5,
#         args=(message.from_user.id,)
#     )
#     await message.answer("Perfect!")
#
#
# async def send_notif(chat_id: int):
#     await bot.send_message(
#         chat_id=chat_id,
#         text='Hello'
#     )

