from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

n_full_view = 'Общий обзор'
n_lists_of_assets = 'Список активов'


b_full_view = KeyboardButton(n_full_view)
b_lists_of_assets = KeyboardButton(n_lists_of_assets)


kb_client = ReplyKeyboardMarkup(resize_keyboard=True)  # , one_time_keyboard=True) # 1ый параметр - меняет вид клавиатуры, второй параметр - прячет клавиатуры после нажатия


kb_client.add(b_full_view).add(b_lists_of_assets)
