from datetime import datetime


class BaseStorage:
    def __init__(self):
        pass

    def save_request_response_for(self, when: datetime, content: dict):
        pass

    @staticmethod
    def time_specific_key(when: datetime):
        return when.strftime("%Y-%m-%d-%H-%M")
