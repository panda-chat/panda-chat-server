import json
from django.utils import timezone


def to_text_json_object(text, *, id, sender, time):
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": {"id": str(sender.id), "name": sender.username},
        "text": str(text),
    }


def to_image_json_object(image, *, id, sender, time):
    return {
        "id": str(id),
        "time": int(time.timestamp()),
        "sender": {"id": str(sender.id), "name": sender.username},
        "image": {
            "url": f"{image.url}",
            "width": str(image.width),
            "height": str(image.height),
        },
    }


def to_code_json_object(code):
    return {"code": code}


def to_text_json(text, *, id, sender, time):
    return json.dumps(to_text_json_object(text, id=id, sender=sender, time=time))


def to_image_json(image, *, id, sender, time):
    return json.dumps(to_image_json_object(image, id=id, sender=sender, time=time))


def to_code_json(code):
    return json.dumps(to_code_json_object(code))
