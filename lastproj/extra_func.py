import logging
import string

from aiogram import Bot, Dispatcher, executor
import creds.ApiKeys
import json, string

API_TOKEN = creds.ApiKeys.tbot_api
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
# bot = Bot(token=os.getenv(API_TOKEN))
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот вышел в онлайн')

async def on_shutdown(_):
    print('Бот ушел в оффлайн')







"""Reaction on something text"""
@dp.message_handler(commands=['start', 'help'])
async def first_text(message):
    try:
        await bot.send_message(message.chat.id, '<b>Hello</b>', parse_mode='html')
        await message.delete()
    except:
        await message.reply('Напишите боту \nhttps://t.me/FirstStock_bot')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    print('Extra_func Page <<<')
