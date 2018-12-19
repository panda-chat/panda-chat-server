from channels.generic.websocket import WebsocketConsumer
from .models import Client


class ChatConsumer(WebsocketConsumer):

    consumers = {}
    next_consumer_id = 0

    def connect(self):
        self.user = Client(user_name=None, address=self.scope["client"][0])

        self.accept()
        self.send(text_data="[What is your name?]")

    def receive(self, *, text_data):
        if self.user.user_name != None:
            self.user.message_set.create(content=text_data)
            ChatConsumer.broadcast(f"{self.user.user_name}: {text_data}")

        else:
            self.user.user_name = text_data
            self.user.save()
            ChatConsumer.add_consumer(self)
            ChatConsumer.broadcast(f"[{self.user.user_name} has joined the chat.]")

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
