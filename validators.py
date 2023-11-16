import re
from datetime import datetime
from typing import Any

import phonenumbers


def is_phone_number(value: str) -> bool:
    """Checks whether the value is a phone number."""
    return "+" in value


def is_email(value: str) -> bool:
    """Checks whether the value is an email."""
    return "@" in value


def is_date(value: str) -> bool:
    """Checks whether the value is a date."""
    value = value.replace("-", "").replace(".", "")
    return value.isnumeric()


def validate_date(date: str) -> bool:
    """Returns true if the date is valid, otherwise false."""
    try:
        datetime.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False


def validate_phone_number(number: str) -> bool:
    """Returns true if the phone number is valid, otherwise false."""
    parsed_number = phonenumbers.parse(number)
    return phonenumbers.is_valid_number(parsed_number)


def validate_email(email: str) -> bool:
    """Returns true if the email is valid, otherwise false."""
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))


def is_field_valid(value: Any, field_type: str) -> bool:
    """Returns true if the field has correct field_type value."""
    field_validators_map = {
        "PHONE": validate_phone_number,
        "EMAIL": validate_email,
        "DATE": validate_date,
    }
    try:
        validator = field_validators_map[field_type]
        return validator(value)
    except KeyError:
        return True


def infer_field_types(data: dict) -> dict:
    """Assign field type to the data fields."""
    field_type_determiners_map = {
        "PHONE": is_phone_number,
        "EMAIL": is_email,
        "DATE": is_date,
    }
    data_types = {}
    for key, value in data.items():
        for field_type, validator in field_type_determiners_map.items():
            if validator(value):
                data_types[key] = field_type
                break
            else:
                data_types[key] = "TEXT"
    return data_types
