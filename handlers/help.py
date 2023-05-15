from config import bot
from aiogram import types


async def help_handler(message: types.Message):
    """
    Функция возвращает меню/команды.
    :param message:
    :return: list commands
    """
    await bot.send_message(message.from_user.id, f"commands:\n"
                                                 f"/start: greeting you\n"
                                                 "/help: helping you\n"
                                                 "/myinfo: information of user\n"
                                                 "/picture: your picture")
