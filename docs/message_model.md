# Message Model

There are three formats for messages, one for text messages, one for image messages, and one for codes from the server rather than from another client. Messages' formats can be determined by whether they have a `text` property, an `image` property, or a `code` property.

## Text Message Model

* `text`, string - text of the message
* `id`, string - UUID identifying the message
* `sender` - details about the sender of the message
  * `id`, string - UUID identifying the sender
  * `name`, string - username of the sender
  * `color`, string - color of the sender as an HTML-style hexadecimal string, e.g. #FF00FF for magenta
* `time`, int - UNIX timestamp of when the message was first received by the server

```json
{
    "text": "a message",
    "id": "48efe860-6595-4961-9b35-e17acf2d7165",
    "sender": {
        "id": "c037bcd8-05f3-42d1-8001-146616db60ca",
        "name": "someone",
        "color": "#9000FF"
    },
    "time": 1545431032
}
```

## Image Message Model

* `image` - details about the image of the message
  * `url` - url of the image
  * `width` - width of the image
  * `height` - height of the image
* `id`, string - UUID identifying the message
* `sender` - details about the sender of the message
  * `id`, string - UUID identifying the sender
  * `name`, string - username of the sender
  * `color`, string - color of the sender as an HTML-style hexadecimal string, e.g. #FF00FF for magenta
* `time`, int - UNIX timestamp of when the message was first received by the server

```json
{
    "image": {
        "url": "/static/user_images/345d284c-4c8f-4c7c-a262-141b158ec177.png",
        "width": "225",
        "height": "287"
    },
    "id": "48efe860-6595-4961-9b35-e17acf2d7165",
    "sender": {
        "id": "c037bcd8-05f3-42d1-8001-146616db60ca",
        "name": "someone",
        "color": "#9000FF"
    },
    "time": 1545431032
}
```

## Code Message Model

```json
{
    "code": "AUTH_SUCCESS"
}
```
