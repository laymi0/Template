from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio

from data import config




from middlewares.throttling import ThrottlingMiddleware

from handlers.users import register_start
from handlers.errors import register_error

from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.sql import dbwork



async def on_startup(dispatcher, bot):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher, bot)


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    db = dbwork('chat.db')
    

    await on_startup(dp, bot)
    print("Отправил администраторам сообщения.")


    dp.middleware.setup(ThrottlingMiddleware())

    register_start(dp)
    register_error(dp)
    print("Все хендлеры работают.")


    try:
        await dp.start_polling()
        
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())

