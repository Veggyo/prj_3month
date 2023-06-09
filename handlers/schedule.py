from aiogram import types
from config import bot, scheduler


async def start_reminder(message: types.Message):
    """
     Удаляем первые 8 символов ("Напомни ") и запускаем таймер
    """
    text = message.text[8:]
    chat_id = message.from_user.id
    scheduler.add_job(remind_handler, 'interval', minutes=3, args=(text, chat_id,))
    await message.answer(text)


async def remind_handler(text, chat_id):
    """
    функция возвращает текст
    """
    await bot.send_message(chat_id=chat_id, text=text)


async def cancel_notif(message: types.Message):
    scheduler.remove_job(job_id='my sheduler')
    await message.answer("Ваша задача аннулирована")
