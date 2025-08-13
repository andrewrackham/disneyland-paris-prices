import requests

from common import config
from pull_data.aws_orchestrator import AwsOrchestrator
from pull_data.local_orchestrator import LocalOrchestrator
from pull_data.orchestrator import Orchestrator


def run_app(orchestrator: Orchestrator) -> None:
    storage = orchestrator.storage()

    response = requests.post(orchestrator.url(), json=orchestrator.payload())
    response.raise_for_status()
    content = response.json()

    previous_content = storage.load_latest(config.KEY_REQUEST_RESPONSE)

    if not previous_content or previous_content != content:
        storage.save(config.KEY_REQUEST_RESPONSE, orchestrator.datetime(), content)


def lambda_handler(event, context):
    run_app(AwsOrchestrator())
    return {"status": "ok"}


if __name__ == "__main__":
    run_app(LocalOrchestrator())
