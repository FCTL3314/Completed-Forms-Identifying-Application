from typing import Any

from tinydb import TinyDB, where

db = TinyDB("database.json")

initial_db_data = [
    {"name": "First form", "email": "EMAIL", "phone": "PHONE"},
    {"name": "Second form", "email": "EMAIL", "phone": "PHONE", "birth_date": "DATE"},
]  # This data is used for testing, so don't delete it :3


def prepare_db() -> None:
    """
    Clears and creates initial database data before
    application start.
    """
    db.truncate()
    db.insert_multiple(initial_db_data)


def find_matching_template(data_types: dict) -> dict[str, Any] | None:
    """
    Tries to find a template based on fields and their types;
    if found, returns its name, otherwise returns None.
    """
    query = None
    for field, data_type in data_types.items():
        if query is None:
            query = where(field) == data_type
        else:
            query &= where(field) == data_type
    result = db.search(query)  # noqa

    if len(result) > 0:
        template = result[0]
        return template
