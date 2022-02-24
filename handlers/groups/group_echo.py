import logging

from aiogram import types
from data.config import CHANNELS
from filters import IsGroup
from keyboards.inline.subscription import check_button
from loader import bot, dp
from utils.misc import subscriptionmisc


@dp.message_handler(IsGroup())
async def show_channels(message: types.Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        status = await subscriptionmisc.check(user_id=message.from_user.id,
                                              channel=channel)
        if status:
            return
        else:
            invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
            channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
            members = message.from_user.get_mention(as_html=True)
            await message.reply(f"{members}, Guruhga yozish uchun quyidagi kanalga obuna bo'ling: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)
            await message.delete()
    # status = await subscriptionmisc.check(user_id=message.from_user.id,
                                          # channel=channel)


@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    result = str()
    for channel in CHANNELS:
        status = await subscriptionmisc.check(user_id=call.from_user.id,
                                              channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            members = call.from_user.get_mention(as_html=True)
            result += f"{members}, <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        else:
            invite_link = await channel.export_invite_link()
            result += (f"<b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
                       f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")

    await call.message.reply(result, disable_web_page_preview=True)
