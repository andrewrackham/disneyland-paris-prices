import os
from datetime import datetime

from aws.aws_storage import AwsStorage
from base_storage import BaseStorage
from transform_data.orchestrator import Orchestrator


class AwsOrchestrator(Orchestrator):
    __storage: AwsStorage

    def __init__(self):
        super().__init__()
        self.__storage = AwsStorage(os.environ["DATA_BUCKET"])

    def storage(self) -> BaseStorage:
        return self.__storage

    def datetime(self) -> datetime:
        return datetime.now()
