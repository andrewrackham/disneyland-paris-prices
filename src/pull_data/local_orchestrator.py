import argparse
import os
from datetime import datetime

from dateutil import parser as dateutil_parser

from base_storage import BaseStorage
from local.local_storage import LocalStorage
from pull_data.orchestrator import Orchestrator
from pull_data.payload_builder import PayloadBuilder


class LocalOrchestrator(Orchestrator):
    __storage: LocalStorage
    __args: argparse.Namespace
    __datetime: datetime

    def __init__(self):
        super().__init__()
        root = os.path.dirname(f"{os.path.dirname(__file__)}/../../")
        self.__parse_cli_args()
        self.__storage = LocalStorage(f"{root}/data")

    def __parse_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--run-time', default=None)
        parser.add_argument('-u', '--url', default=os.environ['ENDPOINT'])
        parser.add_argument('-s', '--start-date',
                            default=os.environ.get('START_DATE') or PayloadBuilder.DEFAULT_START_DATE)
        parser.add_argument('-e', '--end-date',
                            default=os.environ.get('END_DATE') or PayloadBuilder.DEFAULT_END_DATE)
        parser.add_argument('-a', '--adults',
                            default=os.environ.get('ADULTS') or PayloadBuilder.DEFAULT_ADULTS)
        parser.add_argument('-c', '--children', action='append', default=None)
        self.__args = parser.parse_args()

        if self.__args.children is None:
            if 'CHILDREN' in os.environ:
                self.__args.children = os.environ['CHILDREN'].split(',')
            else:
                self.__args.children = PayloadBuilder.DEFAULT_CHILDREN

        datetime_string = self.__args.run_time if self.__args.run_time else os.environ["RUN_TIME"]
        self.__datetime = dateutil_parser.parse(datetime_string)

    def storage(self) -> BaseStorage:
        return self.__storage

    def url(self) -> str:
        return self.__args.url

    def datetime(self) -> datetime:
        return self.__datetime

    def payload(self) -> dict:
        return PayloadBuilder.build(
            start_date=self.__args.start_date,
            end_date=self.__args.end_date,
            adults=self.__args.adults,
            children=self.__args.children,
        )
