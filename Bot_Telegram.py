from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin
from base_barber import sql_db


async def on_startup(_):
    print('Бот включен')
    sql_db.sql_start()


client.register_handler_client(dp)
admin.register_handlers_admin(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)#skip-блот не будет отвечать на сообщения когда не онлайн