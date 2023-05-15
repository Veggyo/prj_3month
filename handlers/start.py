from aiogram import types
from config import bot


async def start_handler(message: types.Message):
    """
    Функция приветсвует пользователя по нику.
    :param message:
    :return: message.from_user.first_name
    """
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("Магазин:", url='https://google.com')
    )
    kb.add(
        types.InlineKeyboardButton("О нас", callback_data='about')
    )
    kb.add(
        types.InlineKeyboardButton("Address", url='https://github.com/')
    )
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}", reply_markup=kb)
