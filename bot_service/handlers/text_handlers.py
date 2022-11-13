import logging

from aiogram import types

from bot_service.config import dp
from bot_service.db.db_interface import Crud
from bot_service.handlers.button_handlers import Keyboard
from bot_service.utils.city_processor import choose_city
from bot_service.weather_api.weather_utils import get_response_with_temperature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dp.message_handler(text="Temperature in my city")
async def temperature_handler(message: types.Message):
    """if user's city is saved, tries to provide a current temperature"""
    city = Crud().get_chosen_city(message.chat.id)
    logger.debug("city is %r", city)
    if not city:
        reply_text = "Your city isn't chosen. Type the name of the city"
        await message.answer(reply_text, reply_markup=types.ReplyKeyboardRemove())
        return
    reply_text, _ = await get_response_with_temperature(city)
    await message.answer(reply_text)


@dp.message_handler(text="Choose/change my city")
async def change_city_handler(message: types.Message):
    """reminds to type the city"""
    reply_text = "Type the city you want to know a current temperature in"
    await message.answer(reply_text)


@dp.message_handler()
async def new_city_handler(message: types.Message):
    """checks if user's input is a name of the city on the weather site"""
    reply_text = await choose_city(message.chat.id, message.text)
    await message.answer(reply_text, reply_markup=Keyboard.keyboard_markup)
