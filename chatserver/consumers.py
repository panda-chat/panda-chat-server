from channels.generic.websocket import WebsocketConsumer
from .models import Client
from .json_formatter import JsonFormatter


class ChatConsumer(WebsocketConsumer, JsonFormatter):

    consumers = {}
    next_consumer_id = 0

    def connect(self):
        self.user = Client(user_name=None, address=self.scope["client"][0])

        self.accept()
        self.send(text_data=self.format("What is your name?"))

    def receive(self, *, text_data):
        if self.user.user_name != None:
            new_message = self.user.message_set.create(content=text_data)
            ChatConsumer.broadcast(
                self.format(
                    new_message.content,
                    id=new_message.id,
                    sender_id=self.user.id,
                    time=new_message.created,
                )
            )

        else:
            self.user.user_name = text_data
            self.user.save()
            ChatConsumer.add_consumer(self)
            ChatConsumer.broadcast(
                self.format(f"{self.user.user_name} has joined the chat.")
            )

    def disconnect(self, close_code):
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
