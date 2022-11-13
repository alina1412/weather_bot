from aiogram import types

from bot_service.config import dp


@dp.message_handler(commands=["info"])
async def send_info(message: types.Message):
    await message.reply("Hi!\nI was updated at 13.11.22")
