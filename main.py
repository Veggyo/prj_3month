from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.executor import
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello {message.from_user.first_name}")

@dp.message_handler(commands=['help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"commands:\n"
                                                 f"/start: greeting you\n"
                                                 "/help: helping you\n"
                                                 "/myinfo: information of user\n"
                                                 "/picture: your picture")

@dp.message_handler(commands=['myinfo'])
async def start_handler(message: types.Message):
    await message.answer(f"your info: \n"
                         f"id: {message.from_user.id}\n"
                         f"name: {message.from_user.first_name}\n"
                         f"nick: {message.from_user.username}")

@dp.message_handler(commands=['picture'])
async def start_handler(message: types.Message):
    with open('media/img.png', 'rb') as photo:
        await message.answer_photo(photo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
