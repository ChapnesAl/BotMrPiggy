# import logging
# from aiogram import executor, Dispatcher, Bot
# import creds.ApiKeys
#
#
#
#
# API_TOKEN = creds.ApiKeys.tbot_api
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=API_TOKEN)
# # bot = Bot(token=os.getenv(API_TOKEN))
# dp = Dispatcher(bot)
#
#
# async def on_startup(_):
#     print('Бот вышел в онлайн')
#
# async def on_shutdown(_):
#     print('Бот ушел в оффлайн')
#
#
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)


# import logging
# from aiogram import Bot, Dispatcher, executor, types
# import creds.ApiKeys
#
# API_TOKEN = creds.ApiKeys.tbot_api
# logging.basicConfig(level=logging.INFO)
# bot = Bot(token=API_TOKEN)
# # bot = Bot(token=os.getenv(API_TOKEN))
# dp = Dispatcher(bot)
#
# async def on_startup(_):
#     print('Бот вышел в онлайн')
#
# async def on_shutdown(_):
#     print('Бот ушел в оффлайн')
#
# exe = executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)

