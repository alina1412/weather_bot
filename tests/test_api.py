import httpx
import pytest

from bot_service.config import Config


# @pytest.mark.my
async def test_get_weather_data():
    assert Config.weather_token is not None
    city = "Moscow"
    url = "http://api.openweathermap.org" + f"/data/2.5/weather?q={city}"
    params = {
        "units": "metric",
        "appid": Config.weather_token,
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=params)
    assert resp.status_code == 200
