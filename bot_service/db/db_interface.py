class Fake_db:
    db = {}

    @staticmethod
    def db_select(key, chat_id):
        value = Fake_db.db.get(chat_id, {}).get(key, "")
        return value

    @staticmethod
    def db_update(key, value, chat_id):
        chat_dict = Fake_db.db.get(chat_id, {})
        if not chat_dict:
            Fake_db.db[chat_id] = {}
        Fake_db.db[chat_id][key] = value
        print(Fake_db.db)


class Crud:
    def __init__(self) -> None:
        self.db = Fake_db

    def get_chosen_city(self, chat_id: int) -> str:
        return self.db.db_select("city", chat_id)

    def write_chosen_city(self, city: str, chat_id: int) -> None:
        return self.db.db_update("city", city, chat_id)
