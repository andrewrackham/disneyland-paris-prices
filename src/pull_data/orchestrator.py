from typing import Protocol

from base_storage import BaseStorage

MARKET_CODE = "en-gb"
HOTEL_CODE = "DNYH"
LOS_CODE = "4n_5j"


class Orchestrator(Protocol):
    def storage(self) -> BaseStorage:
        pass

    def url(self) -> str:
        pass

    def payload(self) -> dict:
        return {
            "market": MARKET_CODE,
            "startDate": '2025-06',
            "endDate": '2026-03',
            "los": LOS_CODE,
            "hotel": HOTEL_CODE,
            "adult": 2,
            "child": []
        }
