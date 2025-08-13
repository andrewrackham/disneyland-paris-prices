import argparse
import os
from datetime import datetime

from dateutil import parser as dateutil_parser

from base_storage import BaseStorage
from local.local_storage import LocalStorage
from transform_data.orchestrator import Orchestrator


class LocalOrchestrator(Orchestrator):
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
        self.__args = parser.parse_args()

        datetime_string = self.__args.run_time if self.__args.run_time else os.environ["RUN_TIME"]
        self.__datetime = dateutil_parser.parse(datetime_string)

    def storage(self) -> BaseStorage:
        return self.__storage

    def datetime(self) -> datetime:
        return self.__datetime
