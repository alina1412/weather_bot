from aiogram import types

from bot_service.config import dp


class Keyboard:
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    btns_text = ("Temperature in my city", "Choose/change my city")
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))


@dp.message_handler(commands="start")
async def start_cmd_handler(message: types.Message):
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute
    await message.answer(
        "Hi!\nWana know the current temperature?", reply_markup=Keyboard.keyboard_markup
    )
