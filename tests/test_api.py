import pytest
import requests

from bot_service.config import Config


# @pytest.mark.my
async def test_get_weather_data():
    assert Config.weather_token is not None
    city = "Moscow"
    url = (
        "http://api.openweathermap.org"
        + f"/data/2.5/weather?q={city}"
    )
    params = {
        "units": "metric",
        "appid": Config.weather_token,
    }
    resp = requests.get(url, params=params)
    assert resp.ok is True
