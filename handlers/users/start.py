from aiogram import Dispatcher
from aiogram.types import *
from aiogram.dispatcher.filters.builtin import CommandStart



async def bot_start(msg: Message):
    await msg.answer(f"Привет, {msg.from_user.full_name}!")


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
