# Message Model

There are two formats for messages, one for text messages and one for image messages. Messages' formats can be determined by whether they have a `text` property or an `image` property.

## Text Message Model

* `text`, string - text of the message
* `id`, string - UUID identifying the message
* `sender`, string - username of the sender
* `time`, int - UNIX timestamp of when the message was first received by the server

```json
{
    "text": "a message",
    "id": "48efe860-6595-4961-9b35-e17acf2d7165",
    "sender": "someone",
    "time": 1545431032
}
```

## Image Message Model

* `image` - details about the image of the message
  * `url` - url of the image
  * `width` - width of the image
  * `height` - height of the image
* `id`, string - UUID identifying the message
* `sender`, string - username of the sender
* `time`, int - UNIX timestamp of when the message was first received by the server

```json
{
    "image": {
        "url": "/static/user_images/345d284c-4c8f-4c7c-a262-141b158ec177.png",
        "width": "225",
        "height": "287"
    },
    "id": "48efe860-6595-4961-9b35-e17acf2d7165",
    "sender": "someone",
    "time": 1545431032
}
```
