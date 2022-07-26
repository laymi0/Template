import logging

from datetime import datetime
from aiogram import Bot, Dispatcher

from data.config import ADMINS

async def on_startup_notify(dp: Dispatcher, bot: Bot):
    
    me = await bot.get_me()
    
    for admin in ADMINS:
        try:
            
            await dp.bot.send_message(admin, f"<b>В {datetime.now().replace(microsecond=0)} Запущен бот {me.full_name}</b>\n\n"
            f'<b>Информация о боте:\nИмя:</b> <code>{me.full_name}</code>\n'
            f'<b>Юзернейм</b>: <code>{me.username}</code>\n'
            f'<b>Айди: </b><code>{me.id}</code>')

        except Exception as err:
            logging.exception(err)
