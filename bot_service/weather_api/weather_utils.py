import logging

from bot_service.weather_api.weather_connection import get_temperature

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def prepare_query(query):
    query = "+".join(query.split(" "))
    return query


async def get_response_with_temperature(city) -> tuple[str, bool]:
    query = prepare_query(city)
    logger.debug(query)
    try:
        temp = await get_temperature(query)
    except Exception as exc:
        logger.debug(exc)
        return ("Unfortunately, an error occured", False)
    if temp is None:
        return ("We haven't found that city", False)
    return (f"The temperature in the city {city} now is {temp} °C", True)
