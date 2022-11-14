from bot_service.db.db_interface import Crud
from bot_service.weather_api.weather_utils import get_response_with_temperature


def is_english(phrase) -> bool:
    """checks if only letters, spaces, dashes"""
    try:
        phrase.encode(encoding="utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace("-", "")
    return phrase.isalpha()


async def parse_city(city) -> str:
    """makes some validations"""
    city = city.strip()
    while "  " in city:
        city = city.replace("  ", " ")
    if len(city) > 30 or not is_english(city):
        return ""
    return city


async def choose_city(chat_id, city) -> str:
    """tries to check and save the city
    and returns result+temperature or unsuccessful message"""
    parsed_city = await parse_city(city)
    if not parsed_city:
        return "We can't understand. Please, type the name of the city"

    reply_text, success = await get_response_with_temperature(parsed_city)
    if success:
        Crud().write_chosen_city(parsed_city, chat_id)
    return f"Your city is {parsed_city}.\n" + reply_text
