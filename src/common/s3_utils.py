import boto3
import json
from typing import Any

s3 = boto3.client("s3")


def save_json(bucket: str, key: str, data: Any):
    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(data))


def load_json(bucket: str, key: str) -> Any:
    obj = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(obj["Body"].read())
