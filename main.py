from aiogram import executor
from config import dp
from handlers.start import start_handler
from handlers.picture import pic_handler
from handlers.help import help_handler
from handlers.myinfo import myinfo_handler
from handlers.about import about_handler, address_handler
from handlers.botbot import get_stud, process_get_info
from handlers.shop import show_categories


if __name__ == '__main__':
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(get_stud, commands=['students_info'])
    dp.register_message_handler(pic_handler, commands=['picture'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(myinfo_handler, commands=['myinfo'])
    dp.register_message_handler(show_categories, commands=['mentors'])
    dp.register_callback_query_handler(about_handler, lambda cb: cb.data == 'about')
    dp.register_callback_query_handler(address_handler, lambda cb: cb.data == 'address')
    dp.register_callback_query_handler(process_get_info, text='process_get_info')

    executor.start_polling(dp, skip_updates=True)
