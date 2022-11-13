"""
"""
from aiogram import executor

from bot_service import handlers
from bot_service.config import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
