from aiogram import types

from bot_service.config import dp


@dp.message_handler(regexp="(^cat[s]?$|puss)")
async def cats(message: types.Message):
    with open("data/cats.jpg", "rb") as photo:
        await message.reply_photo(photo, caption="Cats are here 😺")
