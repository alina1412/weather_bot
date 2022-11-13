# import asyncio
import logging

import httpx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from bot_service.config import Config


async def get_temperature(city) -> float | None:
    url = Config.weather_url
    url = url + f"?q={city}"
    params = {"units": "metric", "appid": Config.weather_token}
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
        data = resp.json()
        logging.info(data)
        temperature = data.get("main", {}).get("temp", None)
        if temperature is None:
            return
        return round(temperature, 1)
