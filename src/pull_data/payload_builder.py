class PayloadBuilder:
    MARKET_CODE = "en-gb"
    HOTEL_CODE = "DNYH"
    LOS_CODE = "4n_5j"
    DEFAULT_START_DATE = "2025-06"
    DEFAULT_END_DATE = "2026-03"
    DEFAULT_ADULTS = 2
    DEFAULT_CHILDREN = []

    @staticmethod
    def build(start_date: str = DEFAULT_START_DATE, end_date: str = DEFAULT_END_DATE,
              adults: int = DEFAULT_ADULTS, children=None) -> dict:
        if children is None:
            children = PayloadBuilder.DEFAULT_CHILDREN
        return {
            "market": PayloadBuilder.MARKET_CODE,
            "startDate": start_date,
            "endDate": end_date,
            "los": PayloadBuilder.LOS_CODE,
            "hotel": PayloadBuilder.HOTEL_CODE,
            "adult": adults,
            "child": children
        }
