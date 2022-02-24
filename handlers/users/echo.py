from aiogram import types

from filters.private_chat import IsPrivate
from loader import dp




# Echo bot
@dp.message_handler(IsPrivate(),state=None)
async def bot_echo(message: types.Message):
    chat_id = message.from_user.id
    msg_id = message.message_id
    await dp.bot.forward_message("554635623",from_chat_id=chat_id,message_id=msg_id)
