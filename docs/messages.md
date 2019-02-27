# Messages Endpoint

If no `before_id` is given, returns the most recent messages.
If `before_id` is given, returns the messages immediately before the message with the matching id.

Messages are returned in reverse chronological order.

**URL** : `/messages`

**Method** : `GET`

**Query Params** :

* `auth_token` - an authentication token provided by the [Login endpoint](login.md)
* `quantity` - number of messages to return (defaults to 100)
* `before_id` - id of message to look before (defaults to None)

## Success Response

**Code** : `200 OK`

**Content example** (See [Message Model](message_model.md))

```json
[
    {
        "text": "nm hbu",
        "id": "d51b3bac-c3c0-4ed0-b5d9-22db8603b373",
        "sender": "longboy",
        "time": 1545432035
    },
    {
        "text": "what is",
        "id": "d33d5865-769c-45bd-b77b-b86a57a832e7",
        "sender": "angeryperson",
        "time": 1545432029
    },
    {
        "image": {
            "url": "/static/user_images/345d284c-4c8f-4c7c-a262-141b158ec177.png",
            "width": "225",
            "height": "287"
        },
        "id": "bf198dff-4dd0-4a98-8138-f40ea8aaadf5",
        "sender": "longboy",
        "time": 1545432020
    },
    {
        "text": "hi",
        "id": "accc42cf-78a2-441b-a027-110fa950e731",
        "sender": "angeryperson",
        "time": 1545432013
    },
]
```
