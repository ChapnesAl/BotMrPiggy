from aiogram import executor
from create_bot import dp



async def on_startup(_):
    print('Бот ОНлайн')


async def on_shutdown(_):
    print('Бот ОФФлайн')


from handlers import hl_general

client.register_handler_client(dp) #чтобы работало, client должен быть выше other
##other.register_handler_other(dp) # ставится последним



executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
print('Commands page <<<')
