import os
from datetime import datetime

from aws.aws_storage import AwsStorage
from aws.config import get_param
from base_storage import BaseStorage
from pull_data.orchestrator import Orchestrator
from pull_data.payload_builder import PayloadBuilder


class AwsOrchestrator(Orchestrator):
    __storage: AwsStorage

    def __init__(self):
        super().__init__()
        self.__storage = AwsStorage(os.environ["DATA_BUCKET"])

    def storage(self) -> BaseStorage:
        return self.__storage

    def url(self) -> str:
        return get_param('data_url')

    def datetime(self) -> datetime:
        return datetime.now()

    def payload(self) -> dict:
        return PayloadBuilder.build(
            start_date=get_param('start_date'),
            end_date=get_param('end_date'),
            adults=get_param('adults'),
            children=get_param('children'),
        )
