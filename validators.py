import re
from datetime import datetime

import phonenumbers


def is_phone_number(number: str) -> bool:
    """
    Checks whether the value is a phone number type.
    """
    if number[0] != "+":
        number = "+" + number
    try:
        parsed_number = phonenumbers.parse(number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False


def is_email(email: str) -> bool:
    """
    Checks whether the value is an email type.
    """
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))


def is_date(date: str) -> bool:
    """
    Checks whether the value is a date type.
    """
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False


data_types_validators_map = {
    "PHONE": is_phone_number,
    "EMAIL": is_email,
    "DATE": is_date,
}
