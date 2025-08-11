import json
from datetime import datetime

import boto3

from base_storage import BaseStorage


class AwsStorage(BaseStorage):
    def __init__(self, bucket: str):
        super().__init__()
        self.s3 = boto3.client("s3")
        self.bucket = bucket

    def save(self, key: str, when: datetime, content: dict):
        key = f"{key}/{BaseStorage.time_specific_key(when)}.json"
        self.s3.put_object(Bucket=self.bucket, Key=key, Body=json.dumps(content))
