from aiogram import types

from bot_service.config import dp


@dp.message_handler(commands="ask")
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)

    btns_text = ("Yes!", "No!")
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    # adds buttons as a new row to the existing keyboard
    # the behaviour doesn't depend on row_width attribute

    more_btns_text = (
        "I don't know",
        "Who am i?",
        "Where am i?",
        "Who is there?",
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))
    # adds buttons. New rows are formed according to row_width parameter
    # reply - after command typed
    await message.reply("Hi!\nDo you like aiogram?", reply_markup=keyboard_markup)
