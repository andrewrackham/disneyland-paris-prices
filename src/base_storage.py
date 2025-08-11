from datetime import datetime


class BaseStorage:
    def __init__(self):
        pass

    def save(self, key: str, when: datetime, content: dict):
        pass

    @staticmethod
    def time_specific_key(when: datetime):
        return when.strftime("%Y-%m-%d-%H-%M")
