import json
from django.utils import timezone


def to_json_object(body, *, id="", sender_id="app", time=None):
    if time == None:
        time = timezone.now()
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": str(sender_id),
        "body": str(body),
    }


class JsonFormatter:
    @staticmethod
    def format(body, *, id="", sender_id="app", time=None):
        return json.dumps(to_json_object(body, id=id, sender_id=sender_id, time=time))
