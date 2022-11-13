from os import environ

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv()


class Config:
    bot_token = environ.get("bot_token")
    weather_token = environ.get("weather_token")
    DEBUG = environ.get("DEBUG", True) is True

    assert bot_token


# Initialize bot and dispatcher
bot = Bot(token=Config.bot_token)
dp = Dispatcher(bot)
