from aiogram.types import (
    Message, CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton)


async def show_categories(message: Message):
    kb = ReplyKeyboardMarkup()
    kb.add(KeyboardButton("Выбрать ментора"))


    await message.answer("Выберите ментора:", reply_markup=kb)


def keyboard(product_id: int):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("выбрать", callback_data=f"choose_{product_id}"))
    return kb


async def show_mentors(message: Message):
    kb = ReplyKeyboardRemove()
    products = [
        (1, "mentor 1"), (2, "mentor 2"), (3, "mentor 3"), (4, "mentor 4"), (5, "mentor 5")
    ]
    await message.answer("У нас свободны: ", reply_markup=kb)
    for pr in products:
        await message.answer(pr[1], reply_markup=keyboard(pr[0]))

async def buy_product_handler(callback: CallbackQuery):
    print(callback.data)
    pr_id = int(callback.data[6:])
    print(pr_id)
