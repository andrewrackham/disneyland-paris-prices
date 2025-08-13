import json
import os
from datetime import datetime
from typing import Optional

from base_storage import BaseStorage, JsonType


class LocalStorage(BaseStorage):
    def __init__(self, base_dir: str):
        super().__init__()
        self.__base_dir = base_dir

    def save(self, key: str, when: datetime, content: JsonType):
        path = f"{self.__base_dir}/{key}/{BaseStorage.time_specific_key(when)}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w', encoding='utf-8') as file_handle:
            json.dump(content, file_handle, ensure_ascii=False, indent=4)

    @staticmethod
    def __load(path: str) -> JsonType:
        with open(path, 'r', encoding='utf-8') as file_handle:
            data = json.load(file_handle)

        return data

    def load(self, key: str, when: datetime) -> JsonType:
        return self.__load(f"{self.__base_dir}/{key}/{BaseStorage.time_specific_key(when)}.json")

    def load_latest(self, key: str) -> Optional[JsonType]:
        directory = f"{self.__base_dir}/{key}"
        if not os.path.isdir(directory):
            return None

        latest_file = max(os.scandir(directory), default=None, key=os.path.getmtime)
        if not latest_file:
            return None

        return self.__load(latest_file.path)
