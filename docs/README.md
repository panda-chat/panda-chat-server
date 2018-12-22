# API Contract

The API is broken into two pieces, the [WebSocket connection](websocket.md) and a [single REST endpoint](messages.md).

The expectation is that the WebSocket connection is used for live communication, while the REST endpoint is used to view chat history and to recover after connection losses.
