import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(),Command('start',prefixes='/'))
async def bot_start(message: types.Message):
    await message.reply(f"<b>{message.from_user.full_name}!</b> siz guruhdasiz😊")
