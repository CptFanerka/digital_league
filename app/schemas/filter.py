import json

from pydantic import BaseModel, ValidationError


class Filter(BaseModel):
    attribute: str
    value: str


def is_valid_filter_list(data: str) -> bool:
    """Функция для проверки строки filters, получаемой /analytics/query. 
    Проверяет, действительно ли был передан список объектов Filter.
    """
    try:
        filters_list = json.loads(data)
        if isinstance(filters_list, list):
            for filter_dict in filters_list:
                Filter(**filter_dict)
            return True
        return False
    except (ValidationError, json.JSONDecodeError):
        return False
