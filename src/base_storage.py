from datetime import datetime
from typing import Union

JsonType = Union[dict, list]


class BaseStorage:
    def __init__(self):
        pass

    def save(self, key: str, when: datetime, content: JsonType):
        pass

    def load(self, key: str, when: datetime) -> JsonType:
        pass

    @staticmethod
    def time_specific_key(when: datetime):
        return when.strftime("%Y-%m-%d-%H-%M")
