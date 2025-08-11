import argparse
import os

from base_storage import BaseStorage
from local.local_storage import LocalStorage
from pull_data.orchestrator import Orchestrator
from pull_data.payload_builder import PayloadBuilder


class LocalOrchestrator(Orchestrator):
    __storage: LocalStorage
    __args: argparse.Namespace

    def __init__(self):
        super().__init__()
        self.__parse_cli_args()
        self.__storage = LocalStorage(f"{os.path.dirname(__file__)}/../../data")

    def __parse_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('url')
        parser.add_argument('-s', '--start-date', default=PayloadBuilder.DEFAULT_START_DATE)
        parser.add_argument('-e', '--end-date', default=PayloadBuilder.DEFAULT_END_DATE)
        parser.add_argument('-a', '--adults', default=PayloadBuilder.DEFAULT_ADULTS)
        parser.add_argument('-c', '--children', action='append', default=PayloadBuilder.DEFAULT_CHILDREN)
        self.__args = parser.parse_args()

    def storage(self) -> BaseStorage:
        return self.__storage

    def url(self) -> str:
        return self.__args.url

    def payload(self) -> dict:
        return PayloadBuilder.build(
            start_date=self.__args.start_date,
            end_date=self.__args.end_date,
            adults=self.__args.adults,
            children=self.__args.children,
        )
