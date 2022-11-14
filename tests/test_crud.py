from bot_service.db.db_interface import Crud


async def test_insert():
    city = "moscow"
    chat_id = 67890756375938264

    res = Crud().get_chosen_city(chat_id)
    assert res == ""

    Crud().write_chosen_city(city, chat_id)
    res = Crud().get_chosen_city(chat_id)
    assert res == city

