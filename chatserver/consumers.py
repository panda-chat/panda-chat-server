from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):

    consumers = {}
    next_consumer_id = 0

    def connect(self):
        self.username = None

        self.accept()
        self.send(text_data="[What is your name?]")

    def receive(self, *, text_data):
        if self.username != None:
            ChatConsumer.broadcast(f"{self.username}: {text_data}")

        else:
            self.username = text_data
            ChatConsumer.add_consumer(self)
            ChatConsumer.broadcast(f"[{self.username} has joined the chat.]")

    def disconnect(self, message):
        ChatConsumer.remove_consumer(self)

    @classmethod
    def broadcast(cls, message):
        for consumer in cls.consumers.values():
            consumer.send(text_data=message)

    @classmethod
    def add_consumer(cls, consumer):
        consumer.id = cls.next_consumer_id
        cls.next_consumer_id += 1
        cls.consumers[consumer.id] = consumer

    @classmethod
    def remove_consumer(cls, consumer):
        del cls.consumers[consumer.id]
