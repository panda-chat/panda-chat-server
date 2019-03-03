import json
from django.utils import timezone


def to_text_json_object(text, *, id="", sender="Panda Chat", time=None):
    if time == None:
        time = timezone.now()
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": str(sender),
        "text": str(text),
    }


def to_image_json_object(image, *, id, sender, time):
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": str(sender),
        "image": {
            "url": f"{image.url}",
            "width": str(image.width),
            "height": str(image.height),
        },
    }


def to_error_json_object(message):
    return {"error": message}


def to_text_json(text, *, id="", sender="Panda Chat", time=None):
    return json.dumps(to_text_json_object(text, id=id, sender=sender, time=time))


def to_image_json(image, *, id, sender, time):
    return json.dumps(to_image_json_object(image, id=id, sender=sender, time=time))


def to_error_json(message):
    return json.dumps(to_error_json_object(message))
