from common import config
from transform_data.aws_orchestrator import AwsOrchestrator
from transform_data.local_orchestrator import LocalOrchestrator
from transform_data.orchestrator import Orchestrator


def run_app(orchestrator: Orchestrator) -> None:
    storage = orchestrator.storage()
    raw_json = storage.load(config.KEY_REQUEST_RESPONSE, orchestrator.datetime())
    result = transform(raw_json)
    orchestrator.storage().save(config.KEY_TRANSFORMED, orchestrator.datetime(), result)


def transform(raw: dict) -> list:
    rooms = dict()
    for room_data in raw['rooms']:
        rooms[room_data['roomCode']] = room_data['name']

    result = []
    for key, value in raw['dates'].items():
        room_code = value['roomType']
        result.append({
            'date': key,
            'price': value['price'],
            'room_code': room_code,
            'room_name': rooms[room_code] if room_code in rooms else 'Unknown'
        })
    return result


def lambda_handler(event, context):
    run_app(AwsOrchestrator())
    return {"status": "ok"}


if __name__ == "__main__":
    run_app(LocalOrchestrator())
