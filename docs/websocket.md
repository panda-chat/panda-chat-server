# WebSocket Connection

The connection over which messages are sent to/from the client in real-time.

**URL** : `/ws`

## Sending

This connection sends two types of messages, messages from other clients and messages from the server itself. Both types of messages are in JSON and use the [Message Model](message_model.md).

Messages from the server itself have a blank `id`, the `sender` is `"Panda Chat"`, and the `time` is the time that the message was sent. Example:

```json
{
    "text": "So-and-so connected.",
    "id": "",
    "sender": "Panda Chat",
    "time": 1545862359
}
```

## Receiving

This connection receives strings or image blobs. Any image file type that the Python 'imghdr' library recognizes should work.

In most cases, all messages received on this connection are sent to all other connected clients. The message is also saved for later retrieval via the [Messages Endpoint](messages.md).

If this is the first message received from an unknown IP address, the message **will not be sent to other clients** but instead the message string will be saved as the username for that IP address. If the first message received is an image blob instead of a string, the message will be discarded, and the client will be asked for their name again.
