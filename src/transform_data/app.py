from datetime import datetime

from common import config
from transform_data.aws_orchestrator import AwsOrchestrator
from transform_data.local_orchestrator import LocalOrchestrator
from transform_data.orchestrator import Orchestrator


def run_app(orchestrator: Orchestrator) -> None:
    storage = orchestrator.storage()
    raw_json = storage.load(config.KEY_REQUEST_RESPONSE, orchestrator.datetime())
    result = transform(raw_json)
    orchestrator.storage().save(config.KEY_TRANSFORMED, orchestrator.datetime(), result)


def transform(raw: dict) -> dict:
    rooms = dict()
    for room_data in raw['rooms']:
        rooms[room_data['roomCode']] = room_data['name']

    result = dict()
    for key, value in raw['dates'].items():
        date = format_date(key)
        room_code = value['roomType']
        if date not in result:
            result[date] = dict()

        result[date][room_code] = {
            'price': value['price'],
            'room_name': rooms[room_code] if room_code in rooms else 'Unknown'
        }

    return dict(sorted(result.items(), key=lambda item: item[0]))


def format_date(date: str) -> str:
    date_time = datetime.strptime(date, "%d-%m-%Y")
    return date_time.strftime('%Y-%m-%d')


def lambda_handler(event, context):
    run_app(AwsOrchestrator())
    return {"status": "ok"}


if __name__ == "__main__":
    run_app(LocalOrchestrator())
