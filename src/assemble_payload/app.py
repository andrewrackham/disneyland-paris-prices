from assemble_payload.aws_orchestrator import AwsOrchestrator
from assemble_payload.local_orchestrator import LocalOrchestrator
from assemble_payload.orchestrator import Orchestrator
from common import config


def run_app(orchestrator: Orchestrator) -> None:
    result = assemble()
    orchestrator.storage().save(config.KEY_ASSEMBLED, orchestrator.datetime(), result)


def assemble() -> dict:
    return dict()


def lambda_handler(event, context):
    run_app(AwsOrchestrator())
    return {"status": "ok"}


if __name__ == "__main__":
    run_app(LocalOrchestrator())
