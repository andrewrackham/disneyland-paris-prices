from datetime import datetime

import requests

from pull_data.aws_orchestrator import AwsOrchestrator
from pull_data.local_orchestrator import LocalOrchestrator
from pull_data.orchestrator import Orchestrator


def lambda_handler(event, context):
    run_app(AwsOrchestrator())
    return {"status": "ok"}


def run_app(orchestrator: Orchestrator) -> None:
    response = requests.post(orchestrator.url(), json=orchestrator.payload())
    response.raise_for_status()
    content = response.json()
    orchestrator.storage().save('request-response', datetime.now(), content)


if __name__ == "__main__":
    run_app(LocalOrchestrator())
