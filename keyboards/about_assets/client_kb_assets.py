from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

n_t_assets = 'Активы - Тестовый'
n_b_assets = 'Активы - Брокерский'
n_i_assets = 'Активы - ИИС'
n_all_assets = 'Все активы'
n_back_to_start = 'Назад на главную'

b_t_assets = KeyboardButton(n_t_assets)
b_b_assets = KeyboardButton(n_b_assets)
b_i_assets = KeyboardButton(n_i_assets)
b_all_assets = KeyboardButton(n_all_assets)
b_back_to_general = KeyboardButton(n_back_to_start)

kb_client_assets = ReplyKeyboardMarkup(
    resize_keyboard=True)  # , one_time_keyboard=True) # 1ый параметр - меняет вид клавиатуры, второй параметр - прячет клавиатуры после нажатия

kb_client_assets.add(b_t_assets).add(b_b_assets).add(b_i_assets).add(b_all_assets).add(b_back_to_general)
