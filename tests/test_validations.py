from bot_service.utils.city_processor import parse_city


async def test_parse_city():
    for query, res in (
        ("Moscow","Moscow"),
        ("yoshkar-ola ","yoshkar-ola"),
        ("saint     petersburg","saint petersburg"),
        ("fbeabaeefwr", "fbeabaeefwr"),
        ("343v39-,", ""),
        ("city/", ""),
        ("citybiwbiduviwnvwnornownvrbubwibviwbv odnwnvbwirjvnwjnanvewjbvjrbwjbkwjvb", ""),
        ):
        parsed = await parse_city(query)
        assert parsed == res