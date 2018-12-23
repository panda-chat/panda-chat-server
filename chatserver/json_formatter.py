import json
from django.utils import timezone


def to_json_object(body, *, id="", sender="Panda Chat", time=None):
    if time == None:
        time = timezone.now()
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": str(sender),
        "body": str(body),
    }


def to_json(body, *, id="", sender="Panda Chat", time=None):
    return json.dumps(to_json_object(body, id=id, sender=sender, time=time))
