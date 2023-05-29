from aiogram import types
from config import bot, scheduler


async def start_reminder(message: types.Message):
    await message.answer("что именно напомнить?")

async def get_sheduler_message(message: types.Message):
    text = message.text
    print(message.text[8:])# Удаляем первые 8 символов ("Напомни ")
    chat_id = message.from_user.id
    scheduler.add_job(remind_handler, 'interval', seconds=3, args=(text, chat_id,), id='my sheduler')
    await message.answer(f"Напоминание: {text}")


async def remind_handler(text, chat_id):
    await bot.send_message(chat_id=chat_id, text=text)


async def cancel_notif(message: types.Message):
    scheduler.remove_job(job_id='my sheduler')
    await message.answer("Ваша задача аннулирована")