from tinydb import TinyDB, where, Query

db = TinyDB("database.json")

initial_db_data = [
    {"name": "MyFirstForm", "email": "first-email@example.com", "phone": "+7 8 812 234-56-77"},
    {"name": "MySecondForm", "email": "second-email@example.com", "phone": "+7 8 812 234-56-78"},
    {"name": "MyThirdForm", "email": "third-email@example.com", "phone": "+7 8 812 234-56-79"},
]


def prepare_db():
    db.truncate()
    db.insert_multiple(initial_db_data)


def add_to_query_if_not_none_or_assign(query: Query | None, query_to_add: bool) -> Query:
    if query is None:
        query = query_to_add
    else:
        query &= query_to_add
    return query


def find_matching_template(data: dict) -> str | None:
    query = None
    if name := data.get("name"):
        query = add_to_query_if_not_none_or_assign(query, (where("name") == name))
    if phone := data.get("phone"):
        query = add_to_query_if_not_none_or_assign(query, (where("phone") == phone))
    if email := data.get("email"):
        query = add_to_query_if_not_none_or_assign(query, (where("email") == email))
    result = db.search(query)

    if len(result) > 0:
        template = result[0]
        return template["name"]
