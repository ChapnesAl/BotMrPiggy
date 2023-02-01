from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from keyboards.client_kb import kb_client
from math_func.general_review import results_full_assets
from keyboards.about_assets.client_kb_assets import *


# n_b_assets = 'Активы - Брокерский'
# n_i_assets = 'Активы - ИИС'
# n_all_assets = 'Все активы'


async def t_assets(message: types.Message):
    await bot.send_message(message.chat.id, """results_full_assets""")
    await message.delete()


async def back_to_start(message: types.Message):
    await bot.send_message(message.chat.id, reply_markup=kb_client)
    await message.delete()


# # @dp.message_handler(commands=['Полезные материалы'])
# async def helpful_info(message: types.Message):
#     await bot.send_message(message.chat.id, 'Видео: Статьи: Новости:')
#
#
# async def company_support(message: types.Message):
#     await bot.send_message(message.chat.id, 'Напишите ваш вопрос:', reply_markup=ReplyKeyboardRemove()) # последний параметр и аргумент убирают свою клавиатуру


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(t_assets(), Text(equals=n_t_assets))
    dp.register_message_handler(back_to_start, Text(equals=n_back_to_start))
