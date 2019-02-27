# API Contract

First, see [Authentication](authentication.md).

Other than authentication, the API is broken into two pieces, a [WebSocket connection](websocket.md) and a [Messages endpoint](messages.md).

The expectation is that the WebSocket connection is used for live communication, while the REST endpoint is used to view chat history and to recover after connection losses.
