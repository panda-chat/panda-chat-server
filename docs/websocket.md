# WebSocket Connection

The connection over which messages are sent to/from the client in real-time.

**URL** : `/ws`

## Initializing

Before the connection sends/receives messages, it must be initialized with an `auth_token`. The client should simply send the `auth_token` string after the connection is opened.

If `auth_token` is valid, the server will send back a message indicating the client has been connected. The client will then be able to send/receive messages over the connection.

If `auth_token` is invalid, the server will send back a JSON message with the error code `AUTH_TOKEN_INVALID`. The connection will stay open -- the client can retry sending `auth_token` as many times as necessary. Example JSON message:

```json
{
    "error": "AUTH_TOKEN_INVALID"
}
```

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
