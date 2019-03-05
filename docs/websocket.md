# WebSocket Connection

The connection over which messages are sent to/from the client in real-time.

**URL** : `/ws`

## Initializing

Before the connection sends/receives messages, the client must be authorized. When the connection is opened, the client should wait for a response from the server.

  - If the server responds with JSON `{ "code": "AUTH_SUCCESS" }`, the client is already authorized and can immediately send/receive messages. 

  - If the server responds with JSON `{ "code": "AUTH_REQUEST" }`, the client should then send an auth token.

    - If the auth token is valid, the server will send back JSON `{ "code": "AUTH_SUCCESS" }`, indicating the client has been authorized. The client will then be able to send/receive messages over the connection.

    - If the auth token is invalid, the server will send back JSON `{ "code": "AUTH_TOKEN_INVALID" }`. The connection will stay open -- the client can retry sending an auth token as many times as necessary.

## Sending

See [Message Model](message_model.md).

## Receiving

This connection receives strings or image blobs. Any image file type that the Python 'imghdr' library recognizes should work.

In most cases, all messages received on this connection are sent to all other connected clients. The only exception is the auth token message sent after an `AUTH_REQUEST`, which is sent to no one. Messages are also saved for later retrieval via the [Messages Endpoint](messages.md).
