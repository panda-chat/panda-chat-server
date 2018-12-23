from channels.generic.websocket import WebsocketConsumer
from .models import Client
from .json_formatter import to_json as format
from .broadcaster import broadcast, register, unregister


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        address = self.scope["client"][0]
        try:
            self.user = Client.objects.get(address=address)
        except Client.DoesNotExist:
            self.user = Client(user_name=None, address=address)

        self.accept()
        if self.user.user_name == None:
            self.send(text_data=format("What is your name?"))
        else:
            register(self, format(f"{self.user.user_name} connected."))

    def receive(self, *, text_data):
        if self.user.user_name != None:
            new_message = self.user.message_set.create(content=text_data)
            broadcast(
                format(
                    new_message.content,
                    id=new_message.id,
                    sender=self.user.user_name,
                    time=new_message.created,
                )
            )

        else:
            self.user.user_name = text_data
            self.user.save()
            register(self, format(f"{self.user.user_name} joined the chat."))

    def disconnect(self, close_code):
        unregister(self, format(f"{self.user.user_name} disconnected."))
