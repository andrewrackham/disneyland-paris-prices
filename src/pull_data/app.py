import argparse
import os
import sys
from datetime import datetime

import requests

from aws import aws_storage
from base_storage import BaseStorage
from common import config
from local import local_storage

MARKET_CODE = "en-gb"
HOTEL_CODE = "DNYH"
LOS_CODE = "4n_5j"


def lambda_handler(event, context):
    storage = aws_storage.AwsStorage(os.environ["DATA_BUCKET"])
    run_app(config.get_param("data_url"), {
        "market": MARKET_CODE,
        "startDate": "2025-06",
        "endDate": "2026-03",
        "los": LOS_CODE,
        "hotel": HOTEL_CODE,
        "adult": 2,
        "child": [
            "2014-12-31",
            "2021-07-29"
        ]
    }, storage)

    return {"status": "ok"}


def run_app(url: str, body: dict, storage: BaseStorage) -> None:
    response = requests.post(url, json=body)
    response.raise_for_status()
    content = response.json()
    storage.save_request_response_for(datetime.now(), content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('-s', '--start-date', default='2025-06')
    parser.add_argument('-e', '--end-date', default='2026-03')
    parser.add_argument('-a', '--adults', default=2)
    parser.add_argument('-c', '--children', action='append', default=[])
    args = parser.parse_args()

    storage = local_storage.LocalStorage()
    run_app(args.url, {
        "market": MARKET_CODE,
        "startDate": args.start_date,
        "endDate": args.end_date,
        "los": LOS_CODE,
        "hotel": HOTEL_CODE,
        "adult": args.adults,
        "child": args.children
    }, storage)
