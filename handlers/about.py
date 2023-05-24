from aiogram import types


async def about_handler(callback: types.CallbackQuery):
    """
     Функция создает кнопку для вывода информации на экран.
    :param callback:
    :return: about
    """
    await callback.message.answer("О нас: Can you help translate this site into a foreign language?")


async def address_handler(callback: types.CallbackQuery):
    """
    Функция  переходит по ссылке для вывода информации на экран.
    :param callback:
    :return: address
    """
    await callback.message.answer(f"Our address: 2f Cheonggu Bldg 10-31 Gangnam-gu, Seoul, Seoul, Korea, Republic of")


# async def stf(callback: types.CallbackQuery):
#     await callback.message.answer(f'info about students: {get_students}')
