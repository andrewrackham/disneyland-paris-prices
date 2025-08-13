from datetime import datetime
from typing import Protocol

from base_storage import BaseStorage


class Orchestrator(Protocol):
    def storage(self) -> BaseStorage:
        pass

    def datetime(self) -> datetime:
        pass
