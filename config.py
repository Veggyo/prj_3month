from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
scheduler = AsyncIOScheduler()
