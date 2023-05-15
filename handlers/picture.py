from aiogram import types


async def pic_handler(message: types.Message):
    """
    Функция возвращает рандомную картину.
    :param message:
    :return: picture
    """
    with open('media/img.png', 'rb') as photo:
        await message.answer_photo(photo)
