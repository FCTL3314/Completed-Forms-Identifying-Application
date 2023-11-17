from typing import Any

from database import find_matching_template
from validators import data_types_validators_map


def get_form_service(query_params: dict) -> dict[str, Any]:
    field_types = get_field_types(query_params)
    if matching_template := find_matching_template(field_types):
        return {"form_name": matching_template["name"]}
    else:
        return field_types


def get_field_types(data: dict) -> dict:
    """
    Assign field type to the data keys.
    """
    data_types = {}
    for key, value in data.items():
        for field_type, validator in data_types_validators_map.items():
            if validator(value):
                data_types[key] = field_type
                break
        else:
            data_types[key] = "TEXT"
    return data_types
