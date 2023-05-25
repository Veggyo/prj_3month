import types
from db.base import insert_table
from aiogram.types import (
    Message,
    CallbackQuery
)
from aiogram.dispatcher.filters import Text
from aiogram import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
# FSM - Finite state machine
# Конечный автомат


class Survey(StatesGroup):
    mentor_id = State()
    name = State()
    age = State()
    who = State()
    course = State()


async def cancel_survey(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Выход из формы')

async def start_survey(cb: CallbackQuery, state: FSMContext):
    await Survey.mentor_id.set()
    async with state.proxy() as data:
        data['mentor_id'] = int(cb.data.replace('start_survey', ''))

    await Survey.next()
    await cb.bot.send_message(chat_id=cb.from_user.id, text='Введите имя')


async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Survey.next()
    await message.answer("Введите ваш возраст:")


async def process_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer('вводите только цифры')
    elif int(age) > 100 or int(age) < 10:
        await message.answer('Только от 10 до 100')
    else:
        async with state.proxy() as data:
            data['age'] = int(age)

        await Survey.next()
        await message.answer("Укажите кем вы являетесь учитель или студент")


async def process_who(message: Message, state: FSMContext):
    whois = message.text
    if whois.isnumeric():
        await message.answer('только буквы')
    elif not whois.isalpha():
        await message.answer('Только учитель или студент')
    else:
        async with state.proxy() as data:
            data['who'] = str(whois)

    await Survey.next()
    await message.answer("Введите ваше направление: ")


async def course_geek(message: Message, state: FSMContext):
    course = message.text
    if not course.isalpha():
        await message.answer('только буквы')
    else:
        async with state.proxy() as data:
            data['course'] = str(course)
            insert_table(data)

        await message.answer('Спасибо за уделенное время!')
        await state.finish()


def register_fsm_handler(dp: Dispatcher):
    dp.register_callback_query_handler(start_survey, lambda cb: cb.data.startswith('start_survey'))
    dp.register_message_handler(process_name, state=Survey.name)
    dp.register_message_handler(process_age, state=Survey.age)
    dp.register_message_handler(process_who, state=Survey.who)
    dp.register_message_handler(course_geek, state=Survey.course)
    dp.register_message_handler(cancel_survey, state='*', commands='cancel')
    dp.register_message_handler(cancel_survey, Text(equals='cancel', ignore_case=True), state='*')
