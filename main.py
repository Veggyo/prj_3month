from aiogram import executor
from config import dp, scheduler
from handlers.start import start_handler
from handlers.picture import pic_handler
from handlers.help import help_handler
from handlers.myinfo import myinfo_handler
from handlers.about import about_handler, address_handler
from handlers.botbot import get_stud
from handlers.anketa_fsm import register_fsm_handler
from handlers.anketa_fsm import cancel_survey
from aiogram.dispatcher.filters import Text
from handlers.schedule import start_reminder, cancel_notif
from handlers.group_admin import register_admin_handlers


if __name__ == '__main__':
    dp.register_message_handler(cancel_survey, state='*', commands='cancel')
    dp.register_message_handler(cancel_survey, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(get_stud, commands=['students_info'])
    dp.register_message_handler(pic_handler, commands=['picture'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(myinfo_handler, commands=['myinfo'])
    dp.register_callback_query_handler(about_handler, lambda cb: cb.data == 'about')
    dp.register_callback_query_handler(address_handler, lambda cb: cb.data == 'address')
    dp.register_callback_query_handler(start_reminder, lambda mess: mess.text.lower() == 'напомни')
    dp.register_message_handler(cancel_notif, commands=['stop'])
    register_fsm_handler(dp)
    register_admin_handlers(dp)
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
