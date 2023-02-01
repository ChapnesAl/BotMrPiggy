import json
import string
from aiogram import types, Dispatcher
from create_bot import dp

"""Echo"""
# @dp.message_handler()
# async def echo_send(message: types.Message):
#     if message.text == "Привет": # or  "привет"
#         await message.answer("И тебе привет :)")
#     else:
#         await message.answer("Не понял :(((")

# await message.answer(message.text)
# await message.reply(message.text)
# await bot.send_message(message.from_user.id, message.text)

"""Find and del bad words"""
"""
создаем генератор: переменную приводим в низкий регистр, в ней убирает попавшие знаки пунктуации (маскирующие символы),
 далее в нее запускаем слова из текста, учитывая пробелы, и все это сравниваем с нашим списком Json.
"""


# @dp.message_handler()
async def bad_words(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()
    """Examples of answers """
    if message.text == "Привет":  # or  "привет"
        await message.answer("И тебе привет :)")
    # else:
    #     await message.answer("Не понял :(((") # не будет работать


def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(bad_words)
