import os

import boto3

ssm = boto3.client("ssm")


def get_param(name, decrypt=False):
    namespace = os.environ.get("PARAMETER_NAMESPACE", "")
    param_name = f"{namespace}/{name}" if not name.startswith("/") else name
    response = ssm.get_parameter(Name=param_name, WithDecryption=decrypt)
    return response["Parameter"]["Value"]
