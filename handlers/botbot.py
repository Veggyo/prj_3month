from db.base import get_students
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def info_kb(mentor_id):
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.add(InlineKeyboardButton('выбрать ментора', callback_data=f'start_survey {mentor_id}'))
    return kb


async def get_stud(message: types.Message):
    stud = get_students()
    for mentor in stud:
        await message.answer(f"ID: {mentor[0]}\n"
                            f"Name: {mentor[1]}\n"
                            f"Age: {mentor[2]}\n"
                            f"Role: {mentor[3]}\n"
                            f"Specialty: {mentor[4]}\n"
                            f"User ID: {mentor[5]}", reply_markup=info_kb(mentor[0]))
