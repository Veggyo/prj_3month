from aiogram import types


async def myinfo_handler(message: types.Message):
    """
    Функция передает информацию о ползователе.
    :param message:
    :return: id, name, nick
    """
    await message.answer(f"your info: \n"
                         f"id: {message.from_user.id}\n"
                         f"name: {message.from_user.first_name}\n"
                         f"nick: {message.from_user.username}")
