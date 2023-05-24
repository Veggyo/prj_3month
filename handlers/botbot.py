from db.base import get_students, get_mentor
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram.dispatcher import FSMContext

async def get_stud(message: types.Message):
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(
        InlineKeyboardButton('Узнать info', callback_data='process_get_info')
    )
    stud = get_students()

    i = 0
    for i in range(len(stud)):
        mentor = stud[i]
        await message.answer(f"ID: {mentor[0]}\n"
                             f"Name: {mentor[1]}\n",
                             reply_markup=kb)

async def process_get_info(callback_query: types.CallbackQuery, state: FSMContext):
    mentor_id = callback_query.data.split()[0]

    # Получите информацию о менторе из функции get_mentor
    mentor = get_mentor(int(mentor_id))

    if mentor:
        response = f"ID: {mentor[0]}\n"
        response += f"Name: {mentor[1]}\n"
        response += f"Age: {mentor[2]}\n"
        response += f"Role: {mentor[3]}\n"
        response += f"Specialty: {mentor[4]}\n"
        response += f"User ID: {mentor[5]}\n"

        await callback_query.answer()
        await bot.send_message(callback_query.from_user.id, response)
    else:
        await callback_query.answer("Mentor not found")  # Ответ, если ментор не найден







