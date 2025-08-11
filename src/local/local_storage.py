import json
import os
from datetime import datetime

from base_storage import BaseStorage

class LocalStorage(BaseStorage):
    def __init__(self, base_dir: str):
        super().__init__()
        self.__base_dir = base_dir

    def save(self, key: str, when: datetime, content: dict):
        path = f"{self.__base_dir}/{key}/{BaseStorage.time_specific_key(when)}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as file_handle:
            json.dump(content, file_handle, ensure_ascii=False, indent=4)
