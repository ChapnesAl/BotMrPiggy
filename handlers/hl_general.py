from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import bot
from keyboards.about_assets import client_kb_assets
from math_func.general_review import results_full_assets
from keyboards.client_kb import *


async def base_commands(message: types.Message):
    await bot.send_message(message.chat.id, '<b>Bot is working</b>', parse_mode='html', reply_markup=kb_client) # добавлен параметр который поднимает свою клавиатуру
    await message.delete()


async def full_view(message: types.Message):
    await bot.send_message(message.chat.id, results_full_assets)
    await message.delete()


async def lists_of_assets(message: types.Message):
    await bot.send_message(message.chat.id, reply_markup=client_kb_assets)
    await message.delete()

# # @dp.message_handler(commands=['Полезные материалы'])
# async def helpful_info(message: types.Message):
#     await bot.send_message(message.chat.id, 'Видео: Статьи: Новости:')
#
#
# async def company_support(message: types.Message):
#     await bot.send_message(message.chat.id, 'Напишите ваш вопрос:', reply_markup=ReplyKeyboardRemove()) # последний параметр и аргумент убирают свою клавиатуру


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(base_commands, commands=['start', 'help'])
    dp.register_message_handler(full_view, Text(equals=n_full_view))
    dp.register_message_handler(lists_of_assets, Text(equals=n_lists_of_assets))
    # dp.register_message_handler(helpful_info, commands=['Полезные_материалы'])
    # dp.register_message_handler(company_support, commands=['Задать_вопрос'])

