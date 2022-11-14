import httpx
import pytest

from bot_service.config import Config
from bot_service.weather_api.weather_utils import get_response_with_temperature

# @pytest.mark.my
async def test_get_weather_data():
    assert Config.weather_token is not None
    for city in ("Moscow", "yoshkar-ola", "saint petersburg"):
        url = "http://api.openweathermap.org" + f"/data/2.5/weather?q={city}"
        params = {
            "units": "metric",
            "appid": Config.weather_token,
        }
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, params=params)
            assert resp.status_code == 200


async def test_get_response_with_temperature_success():
    for city in ("Moscow", "yoshkar-ola", "saint petersburg"):
        _, success = await get_response_with_temperature(city)
        assert success


async def test_get_response_with_temperature_unsuccessful():
    for city in ("Mos cow", "35t54gb", "bevfaevfwv", ""):
        _, success = await get_response_with_temperature(city)
        assert not success