import json
from datetime import datetime

from base_storage import BaseStorage

class LocalStorage(BaseStorage):
    def save_request_response_for(self, when: datetime, content: dict):
        key = f"../../data/{BaseStorage.time_specific_key(when)}-request-response.json"
        with open(key, 'w', encoding='utf-8') as file_handle:
            json.dump(content, file_handle, ensure_ascii=False, indent=4)
